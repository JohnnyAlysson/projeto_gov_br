from flask import Flask, render_template , url_for

from routes.home import home_route
from routes.clients import clients_route

#inicialização
app = Flask(__name__)

#roteamento
app.register_blueprint(home_route)
app.register_blueprint(clients_route)


if __name__== "__main__":
    app.run(debug=True)
