# Se importa la clase db desde el módulo utils.db
from utils.db import db

# Se define la clase Contact que hereda de la clase Model del módulo db
class Contact(db.Model):
    # Se define la columna id como un entero y se establece como clave primaria
    id= db.Column(db.Integer, primary_key=True)
    # Se define la columna fullname como una cadena de caracteres de hasta 100 caracteres
    fullname=db.Column(db.String(100))
    # Se define la columna email como una cadena de caracteres de hasta 100 caracteres
    email=db.Column(db.String(100))
    # Se define la columna phone como una cadena de caracteres de hasta 100 caracteres
    phone=db.Column(db.String(100))
    
    # Se define el método constructor de la clase Contact
    def __init__(self,fullname,email,phone ):
        # Se inicializan las variables fullname, email y phone
        self.fullname=fullname
        self.email   =email
        self.phone   =phone
