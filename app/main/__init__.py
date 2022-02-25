from flask import Blueprint
# import views
# import error
main = Blueprint('main', __name__)

from . import views, error
