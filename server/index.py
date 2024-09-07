# Flask app
from flask import Flask, request, jsonify   
from flask_cors import CORS

#! UNA VEZ ENTENDIDO EL CÓDIGO, BORRAR LOS COMENTARIOS Y EL CÓDIGO DE EJEMPLO,
#! LUEGO EMPEZAR A ESCRIBIR EL CÓDIGO DE LA APLICACIÓN

from database import DatabaseService

# Se crea una instancia de Flask, Flask es un objeto que se encarga de manejar las rutas y las peticiones que se hagan al servidor
app = Flask(__name__)

# Añadir CORS, que permite que la aplicación de front-end se comunique con el servidor
CORS(app)

# @app.route le dice a python que la función debajo de ella es la que se ejecutará cuando se haga una petición a la ruta especificada
@app.route('/login', methods=['POST']) # POST es el método que se usará para hacer la petición, en este caso se usará POST
def api(): # Función que se ejecutará cuando se haga una petición a la ruta /api, debe de ser la misma que la que se puso en el decorador
    # request.get_json() obtiene los datos que se enviaron en la petición, en este caso se espera que se envíe un json
    data = request.get_json()
    print(data)
    
    # jsonify convierte un diccionario en un json
    datos_random = "Hola mundo"
    return jsonify({'data': datos_random}) # Se regresa un json con la llave 'data' y el valor de la variable datos_random

# Ruta 2, siguiendo el ejemplo de arriba
@app.route('/login', methods=['POST'])
def register():
    data = request.get_json()
    print(data)

    datos_random = "Hola mundo"
    return jsonify({'data': datos_random})


# Ejemplo de cómo usar DatabaseService

db = DatabaseService().get_instance() # Se obtiene la instancia de DatabaseService

## Select
res = db.select_all('tabla', columns="*", where="id = 1") # Selecciona todos los datos de la tabla 'tabla' donde el id sea 1
res = db.select_all('tabla', columns="*", ) # Selecciona todos los datos de la tabla 'tabla', no se necesita el WHERE
res = db.select_all('tabla', columns="columna1,columna2") # Selecciona las columnas 'columna1' y 'columna2' de todos los datos de la tabla 'tabla'
res = db.select_count('tabla', count=23) # Selecciona 23 registros de la tabla 'tabla'
res = db.select_one('tabla', columns="*", where="id = 1 AND name = 'holaa'") # Selecciona un registro de la tabla 'tabla' donde el id sea 1 y el name sea 'holaa'

# Insertar datos
db.insert('tabla', {'columna1': 'valor1', 'columna2': 'valor2'}) # Inserta un nuevo registro en la tabla 'tabla'

# Actualizar datos
db.update('tabla', {'columna1': 'valor1', 'columna2': 'valor2'}, "WHERE id = 1") # Actualiza los datos de la tabla 'tabla' donde el id sea 1

# Eliminar datos
db.delete('tabla', "WHERE id = 1") # Elimina los datos de la tabla 'tabla' donde el id sea 1

# Eliminar todos los datos de una tabla
db.flush('tabla') # Elimina todos los datos de la tabla 'tabla'

# Obtener los headers de una tabla
headers = db.get_headers('tabla') # Obtiene los headers de la tabla 'tabla'

# Exportar los datos de una tabla a un archivo de excel
db.export_to_excel('tabla', 'archivo.xlsx') # Exporta los datos de la tabla 'tabla' al archivo 'archivo.xlsx'

# Importar los datos de un archivo de excel a una tabla
db.import_from_excel('tabla', 'archivo.xlsx') # Importa los datos del archivo 'archivo.xlsx' a la tabla 'tabla'

# Conseguir la cantidad de registros en una tabla
count = db.count('tabla') # Obtiene la cantidad de registros en la tabla 'tabla'

# Ejecutar un comando SQL custom
db.execute('SELECT * FROM tabla WHERE id = 1') # Ejecuta el comando SQL 'SELECT * FROM tabla WHERE id = 1'

# Detiene la conexión a la base de datos
db.close()

# __name__ es una variable que python asigna a los archivos que se están ejecutando, si el archivo se está ejecutando directamente __name__ tendrá el valor de '__main__'
if __name__ == '__main__':
    app.run(port=5000) # Se inicia el servidor en el puerto 5000