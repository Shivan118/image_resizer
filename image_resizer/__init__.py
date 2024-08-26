from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints here if using them
    from .app import create_app as create_app_from_module
    app = create_app_from_module()

    return app
