from flask             import current_app,render_template,request
from flask_menu        import register_menu

from .blueprint import links_blueprint

from . import models

@links_blueprint.route('/links')
@register_menu(links_blueprint, '.links', 'Link',order=2)
def show_links():
    return render_template('links.html',links=current_app.database.paginate(current_app.database.select(models.Link)),sectionname="Links",next=request.path)
