from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello darkness my old friend"

if __name__ == '__main__':
    app.run()