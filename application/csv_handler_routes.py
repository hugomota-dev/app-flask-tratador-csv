from flask import render_template, Blueprint, request, redirect, url_for

# Cria o Blueprint para a área CSV
# Note o prefixo de URL '/csv'
csv_blueprint = Blueprint('csv', __name__, url_prefix='/csv')

@csv_blueprint.route('/select_columns')
def select_columns():
    return render_template('select_columns.html')