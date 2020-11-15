import flask

from infrastructure import request_dict
from infrastructure.view_modifiers import response
from services import user_service
import infrastructure.cookie_auth as cookie_auth
from viewmodels.auth.RegisterViewModel import RegisterViewModel

blueprint = flask.Blueprint('auth', __name__, template_folder='templates')


# SHOW LOGIN FORM
@blueprint.route('/login', methods=['GET'])
@response(template_file='/auth/login.html')
def login_get():
    return {}


# AUTHENTICATE A USER
@blueprint.route('/login', methods=['POST'])
@response(template_file='/auth/login.html')
def login_post():
    data = request_dict.create()

    # get the values from the form
    email = data.email.lower().strip()
    password = data.password.strip()

    # perform data validation
    if not email or not password:
        return {
            'email': email,
            'password': password,
            'error': "Some required fields are missing.",
        }

    # insert the data to the database
    user = user_service.login_user(email, password)
    if not user:
        return {
            'email': email,
            'password': password,
            'error': "The account does not exist."
        }

    resp = flask.redirect('/')
    # create a session for the user
    cookie_auth.set_auth(resp, user.user_id)
    # redirect to the screen page

    return resp


# VIEW THE REGISTRATION FORM
@blueprint.route('/register', methods=['GET'])
@response(template_file='/auth/register.html')
def register_get():
    return {
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request)
    }


# REGISTER NEW USER
@blueprint.route('/register', methods=['POST'])
@response(template_file='/auth/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()

    # insert the data to the database
    user = user_service.create_user(vm.name, vm.email, vm.password)
    if not user:
        return vm.to_dict()

    resp = flask.redirect('/')
    # create a session for the user
    cookie_auth.set_auth(resp, user.user_id)
    # redirect to the screen page

    return resp


# END USER'S SESSION
@blueprint.route('/logout', methods=['POST'])
def logout():
    resp = flask.redirect('/login')
    # create a session for the user
    cookie_auth.logout(resp)
    # redirect to the screen page

    return resp
