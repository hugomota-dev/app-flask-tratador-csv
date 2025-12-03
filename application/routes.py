import io
import base64
import pandas as pd
from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response

# Criamos um "grupo" de rotas chamado main
main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    # Se alguém acessar a página (GET), mostra o formulário
    if request.method == "GET":
        return render_template("index.html")