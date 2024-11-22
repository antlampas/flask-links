from flask          import current_app,request,redirect,render_template,url_for
from flask_menu     import current_menu
from flask_security import auth_required
from flask_login    import current_user
from wtforms        import Label
from bleach         import clean

from .blueprint     import links_blueprint

from .models        import Link
from .forms         import linkForm

@links_blueprint.route('/add',methods = ['GET','POST'])
@auth_required()
def add_link():
    link_form = linkForm()
    link_form.submit.label = Label(link_form.submit.id,"Add")
    if request.method == 'POST':
        current_app.logger.info(current_user.username + " sent a new link to " + clean(request.form['name']))
        link      = Link()
        link.name = clean(request.form['name'])
        link.url  = clean(request.form['url'])
        current_app.database.session.add(link)
        current_app.database.session.commit()
        current_app.logger.info("Link to " + clean(request.form['name']) + " added by " + current_user.username)
        return redirect(url_for('links.show_links'))
    return render_template('addLink.html',form=link_form,sectionname="Link")

current_menu.register(text='Add',external_url=url_for('add_link'),logged_only=True)
