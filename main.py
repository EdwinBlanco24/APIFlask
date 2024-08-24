''' importamos las librerias a utilizar
    creamos uan app y definimos a Flask como nuestro server
    Usamos decorador con la app y definimos una ruta URI
'''
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/")

#define una funcion que retorna un valor

def root():
    return "Edwin Blanco"

'''Creamos una app con una ruta /personas y utilizamos el metodo POST.
    definimos la función, capturamos los datos (data)con el request y retornamos
    los datos por medio jsonify, Ademas el cod. 201 nos confirma que la info. se creo.
'''
@app.route("/personas", methods=["POST"])
def create_persons():
    data = request.get_json()
    return jsonify(data), 201
    
if __name__ == "__main__":
    app.run(debug=True)