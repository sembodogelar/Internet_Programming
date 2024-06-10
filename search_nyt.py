import csv
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
    articles = []
    
    for doc in docs:
        article_web_url = doc["web_url"]
        article_headline = doc["headline"]["main"]
        print(f"{article_headline} ({article_web_url})")
        articles.append({"headline": article_headline, "url": article_web_url})
    
    return articles

def save_to_csv(articles, filename="articles.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["headline", "url"])
        writer.writeheader()
        for article in articles:
            writer.writerow(article)

all_articles = []

while True:
    search_term = input("Your search term: ")
    if not search_term:
        break
    search_results = search_articles(search_term)
    articles = display_results(search_results)
    all_articles.extend(articles)

# Save all collected articles to a CSV file
save_to_csv(all_articles)
