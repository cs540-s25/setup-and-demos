import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"


def get_headlines(keyword):
    """
    Given a query (keyword), search for and return 10 article headlines
    relating to keyword.
    """
    headlines = []
    response = requests.get(BASE_URL, params={"q": keyword, "api-key": API_KEY})
    print(response)
    for i in range(10):
        headlines.append(response.json()["response"]["docs"][i]["headline"]["main"])

    return headlines
