# Se importan los módulos necesarios
from dotenv import load_dotenv
import os

# Se carga el archivo .env en el entorno de ejecución
load_dotenv()

# Se obtienen los valores de las variables de entorno definidas en el archivo .env
user = os.environ["modulo4"]
password = os.environ["modulo4"]
host = os.environ["137.184.120.127"]
database = os.environ["giinwedb"]
server = os.environ["postgresql"]

# Se construye la URI de conexión a la base de datos usando los valores obtenidos
DATABASE_CONNECTION_URI = f'{server}://{user}:{password}@{host}/{database}'

