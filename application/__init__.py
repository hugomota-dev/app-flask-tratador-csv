from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from application.main_routes import main_blueprint
    from application.csv_handler_routes import csv_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(csv_blueprint)

    return app
