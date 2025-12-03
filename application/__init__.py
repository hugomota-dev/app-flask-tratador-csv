from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SECRET_KEY'] = 'jduAjlkf&2j4FmtGDj3!@#E4k3nD9$z'

    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)
    

    return app
