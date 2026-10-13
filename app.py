import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

page = "https://quotes.toscrape.com/"
quotes_list = []

while True:
    response = requests.get(page)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Here we mention the CSS class selectors in order to get access over certain HTML scope.
    quotes = soup.select(".quote")

    for quote in quotes:

        # Here we mention the CSS class selectors in order to get access over certain HTML scope.
        text = quote.select_one(".text").get_text(strip=True)

        author = quote.select_one(".author").get_text(strip=True)

        author_href = quote.select_one('small.author + a')["href"]
        author_link = urljoin(page, author_href)

        tags = [tag.get_text(strip=True) for tag in quote.select(".tag")]

        quote_to_append = {
            "text": text,
            "author": author,
            "author_link": author_link,
            "tags": tags
        }
        quotes_list.append(quote_to_append)

    next_page = soup.select_one("ul.pager li.next a")

    if next_page:
        page = urljoin(page, next_page["href"])

    else:
        break

print(quotes_list)
