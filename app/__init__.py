
import logging
from flask import Flask
from config import config
from .common.errors import configure_api_error_handlers


def create_app(config):
    app = Flask(__name__)
    configure_app(app, config)
    configure_api_error_handlers(app)
    configure_logging(app)
    configure_blueprints(app)
    return app


def configure_app(app, config_name):
    app.config.from_object(config[config_name])
    if not app.debug:
        from flask_sslify import SSLify
        SSLify(app)


def configure_blueprints(app):
    from .api import api_blueprint

    for bp in [api_blueprint]:
        app.register_blueprint(bp)


def configure_logging(app):
    if not app.debug:
        import google.cloud.logging
        client = google.cloud.logging.Client()
        client.setup_logging()
        app.logger.setLevel(logging.INFO)
    else:
        app.logger.setLevel(logging.DEBUG)
