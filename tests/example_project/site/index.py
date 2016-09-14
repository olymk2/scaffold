from flask import Flask
from flask import make_response
from flask.ext.login import LoginManager, login_required
from config import settings

from views.profile_pages import profile
from views.example_page import home
from authorize import authorize_pages, login_manager

web_app = Flask(__name__, static_url_path='/static')
web_app.config['PROPAGATE_EXCEPTIONS'] = True
web_app.secret_key = settings.flask_secret_key
login_manager.init_app(web_app)

web_app.register_blueprint(example_pages)


# default homepage
@web_app.route("/", methods=['GET'])
def examples():
    """temporary for testing / examples"""
    return make_response(generate.examples())

#another example page, better off using register bluprint on bigger sites
@web_app.route("/hello_world", methods=['GET'])
def blogs():
    """temporary for testing / examples"""
    return make_response(blog.index())


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000, debug=True)
