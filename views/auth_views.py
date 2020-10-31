import flask

from infrastructure.view_modifiers import response


blueprint = flask.Blueprint('auth', __name__, template_folder='templates')


#SHOW LOGIN PAGE
@blueprint.route('/login')
@response(template_file='/auth/login.html')
def login_get():
    return {}


#REGISTER USER
@blueprint.route('/register')
@response(template_file='/auth/register.html')
def register_post():
    return {}



