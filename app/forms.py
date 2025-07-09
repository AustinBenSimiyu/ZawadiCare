from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, DateField, TextAreaField, 
    FloatField, IntegerField, DateTimeField, SelectField, 
    FileField, SubmitField
)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Optional, NumberRange
from flask_wtf.file import FileRequired, FileAllowed
from app.models.user import User
from wtforms.fields import DateTimeLocalField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional


# Existing Registration and Login forms
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', 
        validators=[DataRequired(), EqualTo('password')])
    due_date = DateField('Due Date', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# New tracking forms
class WeightForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    weight = FloatField('Weight (in lbs)', 
        validators=[DataRequired(), NumberRange(min=0, max=500)])
    notes = TextAreaField('Notes', validators=[Optional()])
    submit = SubmitField('Save Weight')

class MovementForm(FlaskForm):
    date = DateTimeField('Date and Time', 
        format='%Y-%m-%dT%H:%M',  # Specify the format explicitly
        validators=[DataRequired()])
    duration = IntegerField('Duration (minutes)', 
        validators=[DataRequired(), NumberRange(min=0)])
    kick_count = IntegerField('Number of Kicks', 
        validators=[DataRequired(), NumberRange(min=0)])
    notes = TextAreaField('Notes', validators=[Optional()])
    submit = SubmitField('Save Movement')

class AppointmentForm(FlaskForm):
    date = DateTimeLocalField(
        'Date and Time',
        format='%Y-%m-%dT%H:%M',
        validators=[DataRequired()]
    )
    title = StringField('Title', validators=[DataRequired()])
    doctor = StringField('Doctor Name', validators=[Optional()])
    location = StringField('Location', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    submit = SubmitField('Save Appointment')
class PhotoForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    caption = StringField('Caption', validators=[Optional()])
    submit = SubmitField('Upload Photo')

class SymptomForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    nausea = SelectField('Nausea Level', 
        choices=[(str(i), str(i)) for i in range(1, 6)], 
        validators=[Optional()])
    fatigue = SelectField('Fatigue Level', 
        choices=[(str(i), str(i)) for i in range(1, 6)], 
        validators=[Optional()])
    mood = SelectField('Mood', choices=[
        ('happy', 'Happy'),
        ('neutral', 'Neutral'),
        ('anxious', 'Anxious'),
        ('sad', 'Sad'),
        ('irritable', 'Irritable')
    ], validators=[Optional()])
    headache = SelectField('Headache', 
        choices=[('False', 'No'), ('True', 'Yes')],  # Changed this line
        validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    submit = SubmitField('Save Symptoms')
    
class PhotoForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Image files only!')
    ])
    caption = StringField('Caption', validators=[Optional()])
    submit = SubmitField('Upload Photo')