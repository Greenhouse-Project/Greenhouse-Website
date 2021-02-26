from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template # needed for displaying the HTML file

# Local import
from config import app_config
# from app import views   # might not be needed

# Database variable
db =  SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    # Home route
    @app.route('/')
    def Home():
        return render_template('index.html', title='Home')
    
    # # Front Room route
    # @app.route('/front-room')
    # def Front Room():
    #     return render_template('TBD', title='Front Room')
    
    # # Back Room route
    # @app.route('/back-room')
    # def Back Room():
    #     return render_template('TBD', title='Back Room')
    
    # # Outside route
    # @app.route('/outside')
    # def Outside():
    #     return render_template('TBD', title='Outside')
    
    # About route
    @app.route('/about')
    def About():
        return 'The About page is working'
    #     return render_template('TBD', title='About')
    
    
    return app