# Se importan los módulos y clases necesarias
from flask import Blueprint, render_template, request
from models.contacto import Contact
from utils.db import db

# Se define un Blueprint llamado "contacto"
contactos = Blueprint("contacto", __name__)

# Se define la ruta principal "/" para mostrar todos los contactos
@contactos.route("/")
def index():
    # Se obtienen todos los contactos de la base de datos
    contactos = Contact.query.all()
    # Se muestra la plantilla "index.html" y se le pasa la lista de contactos
    return render_template('index.html', contactos=contactos)

# Se define la ruta "/new" para agregar un nuevo contacto
@contactos.route("/new", methods=["POST"])
def new():
    # Se verifica si la petición es una solicitud POST
    if request.method == "POST":
        # Se obtienen los datos del formulario
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        
        # Se crea un nuevo objeto Contact con los datos del formulario
        new_contact = Contact(fullname, email, phone)
        # Se agrega el nuevo objeto a la sesión y se guarda en la base de datos
        db.session.add(new_contact)
        db.session.commit()
        
    # Se devuelve una respuesta indicando que se ha recibido una solicitud con datos
    return 'request con datos'
