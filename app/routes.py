from flask import render_template
from app import app

# Rotas clientes:
    
#     - /clients/ (GET)                   -  Listar clientes
#     - /clients/ (POST)                  -  Inserir cliente no servidor 
#     - /clients/new (GET)                - renderizar o formulário para criar um cliente
#     - /clients/<id> (GET)               - obter dados de um cliente
#     - /clients/<id>/edit  (GET)         - renderizar o formulário para editar um cliente
#     - /clients/<id>/update (PUT)        - atualizar os dados do cliente
#     - /clients/<id>/delete (DELETE)     - deletar os dados do cliente

#     obs: Rotas sem "methods =" são por padrão methods =  "GET"

@app.route("/")
@app.route("/index")
def index():
    dados = {"nome": "fulano","idade": 28, "job": "Customer suport",}

    nome = dados.get("nome")
    idade = dados.get("idade")
    job = dados.get("job")
    return render_template("index.html", nome = nome, idade = idade, job=job)
