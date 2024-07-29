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

# Obtener citas por autor
def get_quotes_by_author(author_name):
    db = connect_to_mongodb()
    quotes_collection = db["quotes"]
    quotes = list(quotes_collection.find({"Author": author_name}, {"_id": 0}))
    return quotes

# Obtener datos del autor por nombre
def get_author_data(author_name):
    db = connect_to_mongodb()
    authors_collection = db["quotes.authors"]
    author = authors_collection.find_one({"Name": author_name}, {"_id": 0})
    return author

def main():
    st.title("Quotes and Authors")

    # Menú de navegación
    menu = ["Home", "Quotes", "Authors"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the Quotes and Authors App! You can navigate through different pages using the dropdown menu on the left.")

    elif choice == "Quotes":
        st.subheader("Quotes")
        quotes_data = get_quotes_data()
        if quotes_data:
            for index, quote in enumerate(quotes_data):
                with st.container():
                    st.write(f"**Quote:** {quote['Quote']}")
                    st.write(f"**Tags:** {quote['Tags']}")
                    st.write(f"**Author:** {quote['Author']}")
                    
                    # Botón desplegable para la biografía
                    with st.expander(f"Biography of {quote['Author']}"):
                        author_data = get_author_data(quote['Author'])
                        if author_data:
                            st.write("**Author Biography:**")
                            st.write(f"**Name:** {author_data['Name']}")
                            st.write(f"**Born Date:** {author_data['Born_Date']}")
                            st.write(f"**Born Location:** {author_data['Born_Location']}")
                            st.write(f"**Description:** {author_data['Description']}")
                        else:
                            st.write(f"No biographical information found for {quote['Author']}.")
                    
                    st.write("---")  # Separador después de cada cita
        else:
            st.write("No quotes found in the database.")

    elif choice == "Authors":
        st.subheader("Authors")
        authors_data = get_authors_data()
        if authors_data:
            for index, author in enumerate(authors_data):
                with st.container():
                    st.write(f"**Name:** {author['Name']}")
                    st.write(f"**Born Date:** {author['Born_Date']}")
                    st.write(f"**Born Location:** {author['Born_Location']}")
                    st.write(f"**Description:** {author['Description']}")
                    
                    # Botón desplegable para las citas
                    with st.expander(f"Quotes by {author['Name']}"):
                        author_quotes = get_quotes_by_author(author['Name'])
                        if author_quotes:
                            for aq in author_quotes:
                                st.write(f"• {aq['Quote']}")
                        else:
                            st.write(f"No quotes found for {author['Name']}.")
                    
                    st.write("---")  # Separador después de cada autor
        else:
            st.write("No authors found in the database.")

if __name__ == "__main__":
    main()