from pymongo import MongoClient
import logging
import os

# Crear directorio de logs si no existe
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Configuración del registro de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'database.log'))
    ]
)

def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["quotes_database"]
        collection = db["quotes"]
        logging.info("Conexión a MongoDB establecida con éxito.")
        return collection
    except Exception as e:
        logging.error(f"Error al conectar a MongoDB: {e}")
        return None

def save_to_mongodb(quotes):
    collection = connect_to_mongodb()
    if collection is not None:
        try:
            collection.insert_many(quotes)
            logging.info("Datos guardados en MongoDB.")
        except Exception as e:
            logging.error(f"Error al guardar datos en MongoDB: {e}")

def save_authors_to_mongodb(authors):
    db = connect_to_mongodb()
    if db is not None:
        try:
            authors_collection = db["authors"]
            authors_collection.insert_many(authors)
            logging.info("Datos de los autores guardados en MongoDB.")
        except Exception as e:
            logging.error(f"Error al guardar datos de los autores en MongoDB: {e}")