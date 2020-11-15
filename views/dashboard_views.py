import flask

from infrastructure import cookie_auth
from infrastructure.view_modifiers import response
import services.user_service as user_service
from viewmodels.auth.IndexViewModel import IndexViewModel

blueprint = flask.Blueprint('dashboard', __name__, template_folder='templates')


#VIEW THE SCREENING FORM

@blueprint.route('/', methods=['GET'])
@response(template_file='/dashboard/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        return flask.redirect('/login')

    return vm.to_dict()


#VIEW ALL PROJECTS

@blueprint.route('/projects', methods=['GET'])
@response(template_file='/dashboard/projects.html')
def projects():
    return {

    }


#VIEW USER PROFILE

@blueprint.route('/profile', methods=['GET'])
@response(template_file='/dashboard/profile.html')
def profile():
    return {}
