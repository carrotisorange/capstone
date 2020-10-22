import flask
import pandas as pd

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('/html/index.html')

@app.route('/login')
def login():
    return flask.render_template('/auth/login.html')


@app.route('/register')
def register():
    return flask.render_template('/auth/register.html')


@app.route('/projects')
def projects():
    return flask.render_template('/html/projects.html')


@app.route('/profile')
def profile():
    return flask.render_template('/html/profile.html')

@app.route('/change-password')
def change_password():
    return flask.render_template('/html/change-password.html')


if __name__ == '__main__':
    app.run(debug=True)


