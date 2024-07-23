from bs4 import BeautifulSoup
import requests
import re

# Obtener la URL

url = 'https://quotes.toscrape.com/'
requests_get = requests.get(url)
get_html = requests_get.text

# Parsear el HTML
soup = BeautifulSoup(get_html, "html.parser")


'''
# Encontrar el primer título

first_title = soup.find('title')
print(first_title.text)

# Encontrar todos los span

all_span = soup.find_all('span')
print(all_span)

# Iteramos sobre ellos y sacamos solo el texto

for quotes in all_span:
    print(quotes.text)

# get_text() para quitar los espacios con strip=True

for quotes in all_span:
    print(quotes.get_text(strip=True))

    '''

# Cogemos las etiqetas que nos interesan, indicando los atributos que queremos

quotes_text = soup.find_all('span', class_ = 'text')
quotes = []

for quote in quotes_text:
    print(quote.text)
    print(" ")
    quotes += quote

print(quotes)

author_names = soup.find_all('small', class_ = 'author')

for name in author_names:
    print(name.text)
    print(" ")

author_about = soup.find_all("a", href = re.compile(r"^/author/"))

for about in author_about:
    full_url = f"https://quotes.toscrape.com{about['href']}"
    print(full_url)
    print(" ")

tags_quotes = soup.find_all('a', class_ = 'tag')

for tag in tags_quotes:
    print(tag.text)
    print(" ")