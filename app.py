import flask


app = flask.Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    from views import dashboard_views
    from views import auth_views
    from views import project_views

    app.register_blueprint(dashboard_views.blueprint)
    app.register_blueprint(auth_views.blueprint)
    app.register_blueprint(project_views.blueprint)


if __name__ == '__main__':
    main()
