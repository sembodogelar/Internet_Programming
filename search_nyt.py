import requests

API_KEY = "TgAinWddVAi8rN7HktGlvqXu5SWk4L0I"
API_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

def search_articles(search_term):
    params = {
        "q": search_term,
        "api-key": API_KEY
    }
    response = requests.get(API_BASE_URL, params=params)
    return response.json()

def display_results(search_results):
    docs = search_results["response"]["docs"]

    for doc in docs:
        article_web_url = doc["web_url"]
        article_headline = doc["headline"]["main"]
        print(f"{article_headline} ({article_web_url})")

while True:
    search_term = input("Your search term: ")
    if not search_term:
        break
    search_results = search_articles(search_term)
    display_results(search_results)
