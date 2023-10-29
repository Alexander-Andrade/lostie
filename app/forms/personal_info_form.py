from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class PersonalInfoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    contact_name = StringField('Contact Name', validators=[DataRequired()])
    contact_phone = StringField('Contact Phone', validators=[DataRequired()])
    extra_contact_name = StringField('Extra Contact Name')
    extra_contact_phone = StringField('Extra Contact Phone')
    description = TextAreaField('Description')
    submit = SubmitField('Save')
