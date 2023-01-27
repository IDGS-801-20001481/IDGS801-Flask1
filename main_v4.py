from flask import Flask, render_template
from flask import request

app =  Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

if __name__ == "__main__":
    app.run(debug = True, port=3001)