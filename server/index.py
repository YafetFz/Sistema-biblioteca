# Flask app
from flask import Flask, request, jsonify   
from flask_cors import CORS

# Se crea una instancia de Flask, Flask es un objeto que se encarga de manejar las rutas y las peticiones que se hagan al servidor
app = Flask(__name__)

# Añadir CORS, que permite que la aplicación de front-end se comunique con el servidor
CORS(app)

# @app.route le dice a python que la función debajo de ella es la que se ejecutará cuando se haga una petición a la ruta especificada
@app.route('/login', methods=['POST'])
def api(): # Función que se ejecutará cuando se haga una petición a la ruta /api, debe de ser la misma que la que se puso en el decorador
    # request.get_json() obtiene los datos que se enviaron en la petición, en este caso se espera que se envíe un json
    data = request.get_json()
    print(data)

    # jsonify convierte un diccionario en un json
    datos_random = "Hola mundo"
    return jsonify({'data': datos_random}) # Se regresa un json con la llave 'data' y el valor de la variable datos_random

# __name__ es una variable que python asigna a los archivos que se están ejecutando, si el archivo se está ejecutando directamente __name__ tendrá el valor de '__main__'
if __name__ == '__main__':
    app.run(port=5000) # Se inicia el servidor en el puerto 5000