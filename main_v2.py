from flask import Flask

app =  Flask(__name__)
@app.route('/')
def index():
    return "Hola Mundo Flask cambios F"

@app.route('/hola')
def hola():
    return "Hola desde hola"

@app.route('/nueva')
def nueva():
    return "Hola desde Nueva"

if __name__ == "__main__":
    app.run(debug = True, port=3001)