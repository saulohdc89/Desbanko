from flask import Flask

app = Flask(__name__)

@app.route("/olamundo/")
def hello_world():
    return {"message": "Olá mundo"}

@app.route("/bemvindo/<usuario>/<int:idade>/<float:altura>/")
def bem_vindo(usuario,idade,altura):
    print(idade)
    return {'Nome':usuario, 
            'Idade': idade,
            'Altura': altura,
            }
