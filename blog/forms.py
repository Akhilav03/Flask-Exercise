from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class UserForm(FlaskForm):
    name = StringField ('Name', validators=[DataRequired()], render_kw={"placeholder":"Your Name...."})
    message = TextAreaField ('Message', render_kw={"rows": 5, "cols": 50, "placeholder":"Your Message...."}, validators=[DataRequired()])
    submit = SubmitField ('Submit')