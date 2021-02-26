'''
This is the application's entry point. 
This file will be used to start the Flask server and launch the application.
'''
import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
