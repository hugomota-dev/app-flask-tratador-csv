from flask import render_template, Blueprint

# Creates a Blueprint instance. This is our "mini-application" or "floor plan".
main_blueprint = Blueprint('main', __name__)


# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')  

# @app.route('/select_columns')
# def select_columns():
#     return render_template('select_columns.html')

# We use main_bp.route() instead of app.route()
@main_blueprint.route('/')
@main_blueprint.route('/index')
def index():
    return render_template('index.html')

@main_blueprint.route('/select_columns')
def select_columns():
    return render_template('select_columns.html')