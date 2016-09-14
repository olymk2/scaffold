from flask import session
from flask import Blueprint
from flask import request
from flask import redirect, abort
from flask.ext.login import current_user, login_required

from scaffold import web
from data.site_user import get_user_details
from data.profile import update_description


profile_pages = Blueprint('profile_pages', __name__, template_folder='templates')


@login_required
@profile_pages.route("/profile", methods=['GET'])
def index():
    web.template.create('Maidstone Hackspace - User profile')
    #~ header('User Profile', url='/profile')
    user = get_user_details({'id': current_user.get_id()}).get()

    name = '%s %s' % (user.get('first_name', ''), user.get('last_name', ''))
    web.page.create('%s - Profile' % name)
    web.columns.create()
    
    web.paragraph.create(
        web.images.create(user.get('profile_image', '/static/images/hackspace.png'), name).add_attributes('width', '200').render()
    )
    web.paragraph.add(name)
    web.paragraph.add('%s' % (user.get('email')))
    web.paragraph.add('Last Login %s' % (user.get('last_login', '')))
    web.paragraph.add('Member since %s' % (user.get('created', '')))
    web.paragraph.add('Description %s' % (user.get('description', '')))
    web.columns.append(web.paragraph.render())

    web.paragraph.create(
        web.link.create(
            'Edit Description',
            'Edit Description',
            '/profile/details'
        ).set_classes('ajaxPopup').render())

    web.columns.append(web.paragraph.render())
    web.page.section(web.columns.render())
    web.template.body.append(web.page.render())

    return web.render()

@login_required
@profile_pages.route("/profile/details", methods=['GET'])
def edit_profile():
    user = get_user_details({'id': current_user.get_id()}).get()
    web.form.create('Update your details', '/profile/update')
    web.form.append(name='description', label='Description', placeholder='This is me i am great')
    web.form.append(name='skills', label='skills', placeholder='python, arduino, knitting')
    web.paragraph.create(web.form.render())
    return web.paragraph.render()

@login_required
@profile_pages.route("/profile/update", methods=['POST'])
def update_profile():
    data = {
        'user_id': current_user.get_id(),
        'skills': request.form.get('skills'),
        'description': request.form.get('description')}
    update_description().execute(data)
    return redirect('/profile')
