from flask              import current_app
from flask_wtf          import FlaskForm
from wtforms            import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired,URL

class linkForm(FlaskForm):
    name   = StringField("Link name",[DataRequired("Name required")])
    url    = StringField("URL",[DataRequired("URL required"),URL("Invalid URL")])
    submit = SubmitField()

class chooseLinkForm(FlaskForm):
    name   = SelectField("Link",[DataRequired("Link name required")])
    submit = SubmitField()
