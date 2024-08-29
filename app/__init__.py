from flask import Flask

def create_app():
    app = Flask(__name__)

    # TODO: Configure secret key and other Flask settings

    from .routes import main
    app.register_blueprint(main)

    # TODO: Add database initialization here if needed

    return app
