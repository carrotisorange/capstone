import flask

from infrastructure.view_modifiers import response


blueprint = flask.Blueprint('dashboard', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='/dashboard/index.html')
def index():
    return {}


@blueprint.route('/projects')
@response(template_file='/dashboard/projects.html')
def projects():
    return {}


@blueprint.route('/profile')
@response(template_file='/dashboard/profile.html')
def profile():
    return {}


#LOGOUT USER
@blueprint.route('/logout')
def logout():
    return 'session has ended!'
