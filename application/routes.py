from application import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')  

@app.route('/select_columns')
def select_columns():
    return render_template('select_columns.html')