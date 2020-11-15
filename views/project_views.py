import flask

from infrastructure.view_modifiers import response
import services.package_service as package_service

blueprint = flask.Blueprint('projects', __name__, template_folder='templates')


#VIEW A PARTICULAR PROJECT
@blueprint.route('/project/<package_name>')
@response(template_file='/projects/show-project.html')
def show_project(package_name:str):
    test_packages = package_service.get_latest_packages()
    return {'package_name':package_name}

