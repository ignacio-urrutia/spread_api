from flask import Flask
from flasgger import Swagger


def create_app():
    app = Flask(__name__)
    Swagger(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
