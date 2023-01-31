from flask import Flask, render_template
from flask import request

app =  Flask(__name__)

@app.route('/calcular', methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route('/calcular', methods=['POST'])
def resultado():
    n1 = request.form.get("textNum1")
    n2 = request.form.get("textNum2")
    res = int(n1) + int(n2)
    return render_template("resultado.html",res,n1,n2)

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

if __name__ == "__main__":
    app.run(debug = True, port=3001)