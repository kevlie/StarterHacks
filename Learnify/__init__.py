import os

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from Learnify.forms import RegistrationForm, LoginForm

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Setting up database for playlists.
    app.config['SECRET_KEY'] = '52bb1d96c13547504affb4c678ffc625'
    p_db = SQLAlchemy(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='index')

    # a simple page that says hello
    @app.route('/')
    def home_page():
        return render_template("mainpage.html")

    @app.route('/about')
    def about_page():
        return render_template("about.html")

    @app.route('/create')
    def create_page():
        return render_template("create.html")

    @app.route('/find')
    def find_page():
        return render_template("find.html")

    @app.route('/register')
    def register():
        form = RegistrationForm()
        return render_template("register.html", title="Register", form=form)

    @app.route('/login')
    def login():
        form = LoginForm()
        return render_template("login.html", title="Login", form=form)

    return app
