from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load th config file
app.config.from_object('config')
