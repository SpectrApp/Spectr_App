from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.models import User, Comment

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"class":"form-control", "id": "inputUsername", "type":"text", "placeholder":"name"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class":"form-control", "id": "inputPassword", "type":"password", "placeholder":"password"})
    remember_me = BooleanField('Запомнить пароль', render_kw={"class":"form-check-input", "id":"inputRememberPassword", "type":"checkbox"})
    submit = SubmitField("Войти", render_kw={"type":"submit", "class":"btn btn-primary"})

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class DeleteProfileForm(FlaskForm):
    submit = SubmitField('Submit')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class HelpForm(FlaskForm):
    pass

class ReplyForm(FlaskForm):
    post = TextAreaField('Write something', validators=[
        DataRequired(), Length(min=1, max=300)])
    submit = SubmitField('Comment')

class PostForm(FlaskForm):
    post = TextAreaField('Write something', validators=[
        DataRequired(), Length(min=1, max=2000)])
    submit = SubmitField('Submit')

class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[
        DataRequired(), Length(min=0, max=300)])
    submit = SubmitField('Submit')

class FileForm(FlaskForm):
    file = FileField(validators=[FileRequired(), FileAllowed(['csv'], 'csv tables only!')])
    submit = SubmitField('Submit')

class AddressForm(FlaskForm):
    address = StringField("Address", render_kw={"class":"form-control", "id": "address", "type":"text", "placeholder":"Адрес"})
    submit = SubmitField(render_kw={ })

class RealEstateForm(FlaskForm):
    address = StringField("Address", render_kw={"class":"form-control", "id": "address", "type":"text", "placeholder":"Адрес"})
    city = StringField("Город", validators=[DataRequired()], render_kw={"class":"form-control", "id": "inputCity", "type":"text", "placeholder":"Город"})
    city_district = StringField("Район", render_kw={"class":"form-control", "id": "inputDistrict", "type":"text", "placeholder":"Район"})
    metro = StringField("Метро", render_kw={"class":"form-control", "id": "inputMetro", "type":"text", "placeholder":"Метро"})
    street = StringField("Улица", render_kw={"class":"form-control", "id": "inputStreet", "type":"text", "placeholder":"Улица"})
    year = StringField("Год постройки", render_kw={"class":"form-control", "id": "inputYear", "type":"text", "placeholder":"Год постройки"})
    floor = StringField("Этаж", render_kw={"class":"form-control", "id": "inputFloor", "type":"text", "placeholder":"Этаж"})
    floors_total = StringField("Этажей в доме", render_kw={"class":"form-control", "id": "inputFloorsTotal", "type":"text", "placeholder":"Этажей в доме"})
    area_total = StringField("Общая площадь", render_kw={"class":"form-control", "id": "inputAreaTotal", "type":"text", "placeholder":"Общая площадь"})
    area_living = StringField("Жилая площадь", render_kw={"class":"form-control", "id": "inputAreaLiving", "type":"text", "placeholder":"Жилая площадь"})
    area_kitchen = StringField("Площадь кухни", render_kw={"class":"form-control", "id": "inputAreaKitchen", "type":"text", "placeholder":"Площадь кухни"})
    rooms = StringField("Количество комнат", render_kw={"class":"form-control", "id": "inputRooms", "type":"text", "placeholder":"Количество комнат"})
    submit = SubmitField("Отправить", render_kw={"type":"submit", "class":"submit action-button"}) 
    