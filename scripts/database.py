from pymongo import MongoClient
import logging
import os
# Crear directorio de logs si no existe
os.makedirs('../logs', exist_ok=True)

# Configuración del registro de logs
logging.basicConfig(filename='../logs/database.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["quotes_database"]
        collection = db["quotes"]
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