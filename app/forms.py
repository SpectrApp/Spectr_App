from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.models import User, Comment

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'class':'form-floating mb-3'})
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login', render_kw={ "class":'btn btn-success'})


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