import io
import base64
import pandas as pd
from flask import Blueprint, render_template, request, flash, redirect, url_for

# Criamos um "grupo" de rotas chamado main
main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET", "POST"])
def index():
    # Se alguém acessar a página (GET), mostra o formulário
    if request.method == "GET":
        return render_template("index.html")
    
    # Método usado para tentar pegar a chave "csv-upload" (atributo name) do formulário
    file = request.files.get("csv-upload")
    if not file:
        flash("Nenhum arquivo enviado.", "error")
        return render_template("index.html")
    

   

    # try:
    #     file_content = file.read()
    #     buffer = io.StringIO(file_content.decode('utf-8'))
    #     df = pd.read_csv(buffer, nrows=0, sep=';')
    #     columns = df.columns.tolist()

    #     csv_base64 = base64.b64encode(file_content).decode('utf-8')
    #     return render_template('index.html', columns=columns, csv_data=csv_base64)
    # except Exception as e:
    #     flash(f'Erro ao processar o arquivo: {str(e)}', 'error')
    #     return render_template('index.html')
