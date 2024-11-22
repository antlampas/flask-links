from flask          import current_app,request,redirect,render_template,url_for
from flask_menu     import current_menu
from flask_security import auth_required
from flask_login    import current_user
from wtforms        import Label
from bleach         import clean

from .blueprint     import links_blueprint

from .models        import Link
from .forms         import chooseLinkForm,linkForm

@links_blueprint.route('/edit',methods = ['GET','POST'])
@auth_required()
def edit_link():
    if request.method == 'POST':
        current_app.logger.info(current_user.username + " is editing link to " + clean(request.form['name']))
        link      = current_app.database.session.execute(current_app.database.select(Link).filter_by(name=clean(request.args['name']))).scalar_one()
        link.name = clean(request.form['name'])
        link.url  = clean(request.form['url'])
        current_app.database.session.commit()
        current_app.logger.info(clean(request.form['name']) + " edited by " + current_user.username)
        return redirect(url_for('links.show_links'))
    elif 'name' in request.args.keys():
        link_form = linkForm()
        link_form.submit.label = Label(link_form.submit.id,"Edit")
        link = current_app.database.session.execute(current_app.database.select(Link).filter_by(name=clean(request.args['name']))).scalar_one()
        link_form.name.data = link.name
        link_form.url.data  = link.url
        return render_template('editLink.html',form=link_form,sectionname="Link")
    else:
        link_form = chooseLinkForm()
        link_form.submit.label = Label(link_form.submit.id,"Edit")
        links = current_app.database.paginate(current_app.database.select(Link))
        link_form.name.choices = [link.name for link in links]
        return render_template('chooseLink.html',form=link_form,sectionname="Link")

current_menu.register_menu(links_blueprint,edit_link,'.links.edit', 'Modifica',logged_only=True)
