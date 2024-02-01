from flask import Flask , render_template
import base
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1>Minha primeira página</h1>"

@app.route("/segunda_pagina")
def segunda_pagina():
    return render_template("index.html")

@app.route("/terceira_pagina")
def terceira_pagina():
    return base.dado

@app.route('/v1/users/idade/<nome>')
def retorna_idade(nome: str):
    if nome == 'johnny':
        return { 'idade':28 }
    else:
    	return { 'idade':' ' }



if __name__ == "__main__":
    app.run()