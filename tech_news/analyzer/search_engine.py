from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": f"(?i){title}"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    try:
        news = search_news(
            {
                "timestamp": {
                    "$eq": datetime.strptime(date, "%Y-%m-%d").strftime(
                        "%d/%m/%Y"
                    )
                }
            }
        )
        return [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {"$regex": f"(?i){tag}"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
