from dotenv import load_dotenv
import os

load_dotenv()

user=os.environ["modulo4"]
password=os.environ["modulo4"]
host=os.environ["137.184.120.127"]
database=os.environ["giinwedb"]
server=os.environ["postgresql"]

DATABASE_CONNECTION_URI=f'{server}://{user}:{password}@{host}/{database}'
