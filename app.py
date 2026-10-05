import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.select(".quote")

for quote in quotes:

    text = quote.select_one(".text").get_text(strip=True)

    author = quote.select_one(".author").get_text(strip=True)

    author_href = quote.select_one('small.author + a')["href"]
    author_link = urljoin(url, author_href)

    tags = [tag.get_text(strip=True) for tag in quote.select(".tag")]

    print(text)
    print(f"{author} - {author_link}")
    print(tags)
    print("-" * 50)
