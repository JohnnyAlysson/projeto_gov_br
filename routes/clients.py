from flask import Blueprint , render_template
from database.fakedb import CLIENTS

clients_route = Blueprint("clients", __name__)

'''
Rotas clientes:
    
    - /clients/ (GET)                   -  Listar clientes
    - /clients/ (POST)                  -  Inserir cliente no servidor 
    - /clients/new (GET)                - renderizar o formulário para criar um cliente
    - /clients/<id> (GET)               - obter dados de um cliente
    - /clients/<id>/edit  (GET)         - renderizar o formulário para editar um cliente
    - /clients/<id>/update (PUT)        - atualizar os dados do cliente
    - /clients/<id>/delete (DELETE)     - deletar os dados do cliente

    obs: Rotas sem "methods =" são por padrão methods =  "GET"


'''

@clients_route.route("/")
def client_list():
    return render_template("client_list.html", clients=CLIENTS)


@clients_route.route("/", methods= "POST")
def insert_client():

    pass

@clients_route.route("/new")
def new_client_form():

    return render_template("new_client_form.html")

@clients_route.route("/<int:client_id>")
def info_client(client_id):

    return render_template("info_client.html")

@clients_route.route("/<int:client_id>/edit")
def edit_client_form(client_id):

    return render_template("edit_client_form.html")

@clients_route.route("/<int:client_id>/update", methods= "PUT")
def update_client(client_id):

    pass

@clients_route.route("/<int:client_id>/delete", methods= "DELETE")
def delete_client(client_id):

    pass