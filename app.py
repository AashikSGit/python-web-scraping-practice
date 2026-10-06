import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

page = "https://quotes.toscrape.com/"

while True:
    response = requests.get(page)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select(".quote")

    for quote in quotes:

        text = quote.select_one(".text").get_text(strip=True)

        author = quote.select_one(".author").get_text(strip=True)

        author_href = quote.select_one('small.author + a')["href"]
        author_link = urljoin(page, author_href)

        tags = [tag.get_text(strip=True) for tag in quote.select(".tag")]

        print(text)
        print(f"{author} - {author_link}")
        print(tags)
        print("-" * 50)

    next_page = soup.select_one("ul.pager li.next a")

    if next_page:
        page = urljoin(page, next_page["href"])

    else:
        break
