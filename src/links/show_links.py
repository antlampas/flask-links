from flask             import current_app,render_template,request
from flask_menu        import current_menu

from .blueprint import links_blueprint

from . import models

@links_blueprint.route('/links')
def show_links():
    return render_template('links.html',links=current_app.database.paginate(current_app.database.select(models.Link)),sectionname="Links",next=request.path)

current_menu.register(text='Link',order=2,external_url=url_for('show_links'))
