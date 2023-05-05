# Se importan los módulos y clases necesarias
from flask import Flask
from rutas.contacto import contactos
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from utils.db import db

# Se crea una instancia de la aplicación Flask
app = Flask(__name__)

# Se configura la conexión a la base de datos y se desactivan las modificaciones automáticas
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Se inicializa la base de datos con la aplicación Flask
db.init_app(app)

# Se registra el Blueprint "contactos" en la aplicación Flask
app.register_blueprint(contactos)
