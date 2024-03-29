from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flasklog.models import User
from flask_login import current_user

class FormPendaftaran(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20) ])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username sudah ada, harap gunakan username yang lain.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email sudah ada, harap gunakan email yang lain.')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class FormUpdateAkun(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20) ])
    email = StringField('Email', validators=[DataRequired(),Email()])
    pict = FileField('Update foto profil', validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Username sudah ada, harap gunakan username yang lain.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email sudah ada, harap gunakan email yang lain.')


class FormPost(FlaskForm):
    judul = StringField('Judul', validators=[DataRequired()])
    konten = TextAreaField('Konten', validators=[DataRequired()])
    post = SubmitField('Posting')




