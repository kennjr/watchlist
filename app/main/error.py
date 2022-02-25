from flask import render_template
from app import app
from urllib import error


# @app.errorhandler(404)
from app.main import main


@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('four0four.html'), 404


@main.app_errorhandler(error.HTTPError)
def http_error(error):
    return render_template('four0four.html'), 404
