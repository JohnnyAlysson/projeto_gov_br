from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')


app.run()
