from flask import Flask
import os

from src.endpoints.users import users
from src.endpoints.parking import parking
from src.endpoints.delegate import delegate
from src.endpoints.admin import admin

def create_app(test_config=None):
    app = Flask(__name__,
    instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(users)
    app.register_blueprint(parking)
    app.register_blueprint(delegate)
    app.register_blueprint(admin)
    return app
