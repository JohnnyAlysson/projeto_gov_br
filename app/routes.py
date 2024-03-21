from flask import render_template
from app import app
# # Rotas ADM:

#       -/admin/ (GET)                    -interface admin
#       -/admin/users(GET)                - listar usuarios com opçãos para remover etc


# Rotas clientes:
    
#       - /users/ (GET)                   -  Listar clientes
#       - /users/ (POST)                  -  Inserir cliente no servidor 
#       - /users/new (GET)                - renderizar o formulário para criar um cliente
#       - /users/<id> (GET)               - obter dados de um cliente
#       - /users/<id>/edit  (GET)         - renderizar o formulário para editar um cliente
#       - /users/<id>/update (PUT)        - atualizar os dados do cliente
#       - /users/<id>/delete (DELETE)     - deletar os dados do cliente

#     obs: Rotas sem "methods =" são por padrão methods =  "GET"

@app.route("/")
# @app.route("/index")
# def index():
#     dados = {"nome": "fulano","idade": 28, "job": "Customer suport",}

#     nome = dados.get("nome")
#     idade = dados.get("idade")
#     job = dados.get("job")
#     return render_template("index.html", nome = nome, idade = idade, job=job)

@app.route("/home")
def home():
    return render_template("home.html")