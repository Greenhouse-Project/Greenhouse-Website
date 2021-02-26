from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask import render_template # needed for displaying the HTML file
from flask_migrate import Migrate # Used to transfer changes from Flask to MySQL
from flask_bootstrap import Bootstrap #used for the login and registration pages

# Local import
from config import app_config

# Using flask-login
from flask_login import LoginManager

# Database variable
db =  SQLAlchemy()

# Need to be after db variable initialization
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    
    migrate = Migrate(app, db)
    
 
    from app import models
    # All of the login and registration pages are run through this blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # All of the standard pages are run through this blueprint    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    return app