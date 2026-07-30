"""News headlines from the BBC via NewsAPI."""

import requests

from olivia.core import config
from olivia.core.speech import speak


def news_from_bbc():
    """Fetch and speak top BBC headlines. Requires NEWS_API_KEY."""
    params = {"source": "bbc-news", "sortBy": "top", "apiKey": config.NEWS_API_KEY}
    res = requests.get("https://newsapi.org/v1/articles", params=params, timeout=10)
    data = res.json()
    titles = [a["title"] for a in data.get("articles", [])]
    for i, title in enumerate(titles, 1):
        print(i, title)
        speak(title)
    return titles
