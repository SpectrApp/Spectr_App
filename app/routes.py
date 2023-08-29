from flask import render_template, flash, redirect, url_for, request, current_app
from app import app, db
from app.forms import (LoginForm, RegistrationForm, EditProfileForm, EmptyForm,
                       PostForm, MessageForm, ReplyForm, DeleteProfileForm, HelpForm,
                       AddressForm, FileForm, RealEstateForm)
from flask_login import current_user, login_user, logout_user, login_required
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from app.models import User, Post, Message, Comment
from datetime import datetime
import os
import pandas as pd
from .utils import get_info_by_address


app.config['DATA_PATH'] = os.path.join('app', 'static', 'data', 'biostats.csv')


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.is_submitted():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('dashboard'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('dashboard'))


DATASET_PATH = None
DATASET_NAME = "example"


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    global DATASET_PATH
    global DATASET_NAME
    # load sample tableDATASET_PATH
    print(DATASET_PATH)
    path = DATASET_PATH
    if DATASET_PATH is None:
        path = os.path.abspath(app.config['DATA_PATH'])
    x = pd.read_csv(path)
    return render_template('dashboard.html', name=DATASET_NAME, data=x.to_html(table_id='datatablesSimple'))


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = FileForm()

    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        filepath = os.path.join(
            app.instance_path, filename
        )
        f.save(filepath)
        # filepath = os.path.abspath(os.path.join('app', 'static', 'data', 'biostats.csv'))
        # x = pd.read_csv(filepath)
        # print(filepath)
        global DATASET_PATH
        global DATASET_NAME
        DATASET_PATH = filepath
        DATASET_NAME = filename
        return redirect(url_for('dashboard'))
        # return render_template('dashboard.html', name=filename, data=x.to_html(table_id='datatablesSimple'))

    return render_template('tables.html', title='Tables',  form=form)


@app.route('/survey', methods=['POST', 'GET'])
@login_required
def survey():
    form = AddressForm()
    realty_form = RealEstateForm()
    ''' 
    if form.is_submitted():
        address_data = get_info_by_address(form.address.data)
        if (address_data is None):
            flash('Invalid address!')
        else:
            print("set")
            if address_data['city'] is not None:
                realty_form.city.data = address_data['city']
            if address_data['city'] is None and address_data['region'] in ['Москва', 'Санкт-Петербург']:
                realty_form.city.data = address_data['region']
            if address_data['city_district'] is not None:
                realty_form.city_district.data = address_data['city_district']
            if address_data['street'] is not None:
                realty_form.street.data = address_data['street']
            if address_data['flat_area'] is not None:
                realty_form.area_total.data = address_data['flat_area']
            # address_data=pd.DataFrame(address_data.items()).to_html(table_id='datatablesSimple')
            return render_template('survey.html', address_form=form, realty_form=realty_form)
    '''
    if realty_form.is_submitted():
        return redirect(url_for('dashboard'))
    else:
        return render_template('survey.html', address_form=form, realty_form=realty_form)
