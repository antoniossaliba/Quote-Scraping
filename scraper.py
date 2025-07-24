from bs4 import BeautifulSoup
import requests


class Scraper:

    def __init__(self, quotes, authors):
        self.quotes = quotes
        self.authors = authors

    def fetch_authors_quotes(self):
        for i in range(1, 11, 1):
            request = requests.get(url=f"https://quotes.toscrape.com/page/{i}/").text
            data = BeautifulSoup(request, "html.parser")
            quotes = data.find_all(attrs={"class": "text"})
            authors = data.find_all(attrs={"class": "author"})
            for quote in quotes:
                self.quotes.append(quote.text)
            for author in authors:
                self.authors.append(author.text)
