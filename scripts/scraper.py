from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import logging
import os
from database import save_to_mongodb, save_authors_to_mongodb

# Crear directorio de logs si no existe
os.makedirs('../logs', exist_ok=True)

# Configuración del registro de logs
logging.basicConfig(filename='../logs/scraper.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Obtener la URL

base_url = 'https://quotes.toscrape.com/'

def get_quotes_from_page(url):
    requests_get = requests.get(url)
    get_html = requests_get.text

    # Parsear el HTML
    soup = BeautifulSoup(get_html, "html.parser")

    #Primero cojo todas las quotes de la url

    quotes_all = soup.find_all('div', class_ = 'quote')

    # Creo la variable quotes en la que guardare los resultados del bucle

    quotes = []

    for quote in quotes_all:
        text_quotes = quote.find('span', class_ = 'text').get_text()
        author_names = quote.find('small', class_ = 'author').get_text()
        author_about_tag = quote.find('a', href = re.compile(r"^/author/"))
        author_about = f"https://quotes.toscrape.com{author_about_tag['href']}"
        tags_quotes_list = []
        for tag in quote.find_all('a', class_ = 'tag'):
            tags_quotes_list.append(tag.get_text())
        tags_quotes = ', '.join(tags_quotes_list)
        temporal_dict = {
                "Quote": text_quotes, 
                "Author": author_names, 
                "Author_About": author_about, 
                "Tags": tags_quotes
            }
        quotes.append(temporal_dict)

    return quotes

def get_all_quotes():
    page = 1
    all_quotes = []

    while True:
        url = f"{base_url}page/{page}/"
        logging.info(f"Accediendo a la URL: {url}")
        quotes = get_quotes_from_page(url)
        if not quotes:
            break
        all_quotes.extend(quotes)
        page += 1

    return all_quotes

def get_author_details(author_url):
    requests_get = requests.get(author_url)
    get_html = requests_get.text

    # Parsear el HTML
    soup = BeautifulSoup(get_html, "html.parser")

    # Extraer detalles del autor
    name = soup.find('h3', class_='author-title').get_text(strip=True)
    born_date = soup.find('span', class_='author-born-date').get_text(strip=True)
    born_location = soup.find('span', class_='author-born-location').get_text(strip=True)
    description = soup.find('div', class_='author-description').get_text(strip=True)

    author_details = {
        "Name": name,
        "Born_Date": born_date,
        "Born_Location": born_location,
        "Description": description,
        "URL": author_url
    }

    return author_details

def get_all_authors(quotes):
    author_urls = list(set([quote["Author_About"] for quote in quotes]))
    all_authors = []

    for author_url in author_urls:
        logging.info(f"Accediendo a la URL del autor: {author_url}")
        author_details = get_author_details(author_url)
        all_authors.append(author_details)

    return all_authors

def main():
    all_quotes = get_all_quotes()
    quotes_df = pd.DataFrame(all_quotes, columns=['Quote', 'Author', 'Author_About', 'Tags'])
    print(quotes_df.head(10))
    save_to_mongodb(all_quotes)
    logging.info("Datos guardados en MongoDB.")

    all_authors = get_all_authors(all_quotes)
    authors_df = pd.DataFrame(all_authors, columns=['Name', 'Born_Date', 'Born_Location', 'Description', 'URL'])
    print(authors_df.head(10))
    save_authors_to_mongodb(all_authors)
    logging.info("Datos de los autores guardados en MongoDB.")

if __name__ == "__main__":
    main()