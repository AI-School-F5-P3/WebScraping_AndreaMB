import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Conectar a la base de datos MongoDB
def connect_to_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["quotes_database"]
    return db

# Obtener datos de la colección de citas
def get_quotes_data():
    db = connect_to_mongodb()
    quotes_collection = db["quotes"]
    quotes = list(quotes_collection.find({}, {"_id": 0}))
    return quotes

# Obtener datos de la colección de autores
def get_authors_data():
    db = connect_to_mongodb()
    authors_collection = db["quotes.authors"]
    authors = list(authors_collection.find({}, {"_id": 0}))
    return authors

# Función principal de la aplicación Streamlit
def main():
    st.title("Quotes and Authors")

    # Menú de navegación
    menu = ["Home", "Quotes", "Authors"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the Quotes and Authors App!")

    elif choice == "Quotes":
        st.subheader("Quotes")
        quotes_data = get_quotes_data()
        if quotes_data:
            quotes_df = pd.DataFrame(quotes_data)
            st.dataframe(quotes_df)
        else:
            st.write("No quotes found in the database.")

    elif choice == "Authors":
        st.subheader("Authors")
        authors_data = get_authors_data()
        if authors_data:
            authors_df = pd.DataFrame(authors_data)
            st.dataframe(authors_df)
        else:
            st.write("No authors found in the database.")

if __name__ == "__main__":
    main()
