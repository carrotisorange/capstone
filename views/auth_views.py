import flask

from infrastructure.view_modifiers import response


blueprint = flask.Blueprint('auth', __name__, template_folder='templates')

#SHOW LOGIN PAGE
@blueprint.route('/login', method=['GET'])
@response(template_file='/auth/login.html')
def login_get():
    return {}

#VALIDATE USER
@blueprint.route('/login', method=['POST'])
@response(template_file='/auth/login.html')
def login_post():
    return {}

#SHOW REGISTER
@blueprint.route('/register', method=['GET'])
@response(template_file='/auth/register.html')
def register_get():
    return {}

#REGISTER USER
@blueprint.route('/register', method=['POST'])
@response(template_file='/auth/register.html')
def register_post():
    return {}
