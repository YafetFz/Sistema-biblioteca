# Flask app
from flask import Flask, request, jsonify   

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    datos_random = "Hola mundo"
    return jsonify({'data': datos_random})

if __name__ == '__main__':
    app.run(port=5000)