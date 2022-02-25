# Where we will initialize our application.

from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
import config

# Initializing application
# The instance_relative_config arg allows us to connect ot the instance dir when the app instance is created
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(DevConfig)
# The app.config.from_pyfile('config.py') line will connect the app instance to the config.py file and appends all its
# content to the app.config
app.config.from_pyfile("config.py")
# Initializing Flask Extensions


from app.main import error, views

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config.config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    # from request import configure_request
    from app.request import configure_request
    configure_request(app)
    return app
