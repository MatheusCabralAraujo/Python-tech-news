import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3)
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    res = Selector(html_content).css("article h2 a::attr(href)").getall()
    return res


# Requisito 3
def scrape_next_page_link(html_content):
    return (
        Selector(html_content)
        .css(".next::attr(href)")
        .get()
    )


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
