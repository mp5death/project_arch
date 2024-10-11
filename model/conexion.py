from pymongo import MongoClient

def conexion():
    # Creacion la conexión con el servidor de MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    # Seleccion de la base de datos
    db = client["Project"]
    return db
