from flask import render_template, Blueprint

# Creates a Blueprint instance. This is our "mini-application" or "floor plan".
main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
@main_blueprint.route('/index')
def index():
    return render_template('index.html')

@main_blueprint.route('/select_columns')
def select_columns():
    return render_template('select_columns.html')