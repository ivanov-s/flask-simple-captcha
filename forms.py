# для работы с формами
from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import TextField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    text = TextField('Комментарий', validators=[DataRequired()])

class ContactRecaptchaForm(ContactForm):
    recaptcha = RecaptchaField()
