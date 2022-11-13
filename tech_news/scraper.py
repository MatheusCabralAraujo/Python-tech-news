import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(html_content)
    items = selector.css(".entry-content p")
    summary = "".join(
        items[0].css("*::text").getall() if items else []
    ).strip()
    res = {
        "url": selector.css('[rel="canonical"]::attr(href)').get(),
        "title": str(selector.css(".entry-title::text").get()).strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".meta-author .author a::text").get(),
        "comments_count": str(
            selector.css("#comments > .title-block::text").get() or ""
        ).split(" ")[0]
        or 0,
        "summary": summary,
        "tags": selector.css('.post-tags ul li [rel="tag"]::text').getall(),
        "category": selector.css(".category-style .label::text").get(),
    }
    return res


# Requisito 5
def get_tech_news(amount):
    res = []
    url = "https://blog.betrybe.com/"
    while len(res) < amount:
        page = fetch(url)
        news = scrape_novidades(page)
        for new in news:
            res.append(scrape_noticia(fetch(new)))
            if len(res) == amount:
                break
        url = scrape_next_page_link(page)

    print(res, amount)
    create_news(res)
    return res
