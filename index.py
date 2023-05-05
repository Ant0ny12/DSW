# Se importan los módulos necesarios
from app import app
from utils.db import db

# Se crea un contexto de aplicación para poder interactuar con la aplicación Flask
with app.app_context():
    # Se crea la estructura de la base de datos si no existe
    db.create_all()

# Si este archivo se está ejecutando como el programa principal...
if __name__ == '__main__':
    # Se inicia la aplicación Flask en modo debug en el puerto 5000
    app.run(host='0.0.0.0', debug=True, port=5000)
