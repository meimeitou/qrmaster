
# from app import models
from flask import Flask, jsonify
from flask_bootstrap import Bootstrap5
from app.api import api
from app.home import app as home
from werkzeug.exceptions import HTTPException, default_exceptions
from config import Config
import logging
from flask_wtf import FlaskForm, CSRFProtect

logging.basicConfig(level=logging.INFO)

def create_app(config_class=Config):
    logging.info(Config.__dict__)
    app = Flask(__name__, static_folder="static", template_folder='templates')
    Bootstrap5(app)
    CSRFProtect(app)

    app.config.from_object(config_class)
    app.register_blueprint(api)
    app.register_blueprint(home)

    def make_json_error(err):
        msg = '{}-{}'.format(str(err), getattr(err, 'data', ''))
        response = jsonify(message=msg)
        response.status_code = (
            err.code if isinstance(err, HTTPException) else 500)
        return response

    for code in default_exceptions.keys():
        app.register_error_handler(code, make_json_error)
    return app
