from flask import Flask, request
from flask_babel import Babel

def get_locale():
    # Try to get the language from a cookie, if not present, use the best match from the Accept-Language header
    lang = request.cookies.get('lang')
    if lang:
        if lang == 'zh':  # Update this to match your locale format
            return 'zh_Hans'  # or 'zh_Hant' based on your requirement
    return request.accept_languages.best_match(['en', 'zh_Hans'])

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize Babel with the locale_selector function
    babel = Babel(app, locale_selector=get_locale)
    @app.context_processor
    def inject_locale():
        return dict(get_locale=get_locale)
    
    from .routes import main
    app.register_blueprint(main)


    return app
