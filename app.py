import os
import flask
import data.db_session as db_sessions


app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        "db.sqlite")

    db_sessions.global_init(db_file)


def register_blueprints():
    from views import dashboard_views
    from views import auth_views
    from views import project_views

    app.register_blueprint(dashboard_views.blueprint)
    app.register_blueprint(auth_views.blueprint)
    app.register_blueprint(project_views.blueprint)


if __name__ == '__main__':
    main()
