from flask import Flask
from server.config import Config
from server.routes.main import main_bp

def create_app():
    app = Flask(__name__, template_folder="../client/templates", static_folder="../client/static")
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
