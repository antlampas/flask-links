from flask             import current_app,request,redirect,Blueprint,render_template,url_for
from flask_sqlalchemy  import SQLAlchemy
from flask_security    import auth_required

from .                 import models
from .                 import forms

links_blueprint = Blueprint('links',__name__,url_prefix='/links',template_folder='template',static_folder='static')
