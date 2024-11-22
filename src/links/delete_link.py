from flask          import current_app,request,redirect,render_template,url_for
from flask_menu     import current_menu
from flask_security import auth_required
from flask_login    import current_user
from wtforms        import Label
from bleach         import clean

from .blueprint     import links_blueprint

from .models        import Link
from .forms         import chooseLinkForm

@links_blueprint.route('/delete',methods = ['GET','POST'])
@auth_required()
def delete_link():
    link_form = chooseLinkForm()
    link_form.submit.label = Label(link_form.submit.id,"Remove")
    if request.method == 'POST':
        current_app.logger.info(current_user.username + " is removing link to " + clean(request.form['name']))
        link      = Link()
        link.name = clean(request.form['name'])
        Link.query.filter_by(name=link.name).delete()
        current_app.database.session.commit()
        current_app.logger.info(clean(request.form['name']) + " removed by " + current_user.username)
        return redirect(url_for('links.show_links'))
    links = current_app.database.paginate(current_app.database.select(Link))
    link_form.name.choices = [link.name for link in links]
    return render_template('deleteLink.html',form=link_form,sectionname="Link")

current_menu.submenu(".links.remove").register(text='Remove',external_url=links_blueprint.url_prefix+"/delete",logged_only=True)
