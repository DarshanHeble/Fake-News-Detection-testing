#import all libraries and variables
import requests
from ..constants import CSE_ID, GOOGLE_API_KEY, BASE_SEARCH_URL
from ..Types.types import FetchedNewsType

"""
code explanation here(coming soon)

"""
def fetchNewsFromGoogle(query)-> list[FetchedNewsType]:
    params = {
        "q": query,
        "cx": CSE_ID,
        "key": GOOGLE_API_KEY,
        "num": 10                   # maximum number of articles to be fetched from Google
    }
    
    response = requests.get(BASE_SEARCH_URL, params=params)
    response.raise_for_status()     # Raise an error for bad requests
    # result = response.json().get("items")
    # result = FetchedNewsType(
    articles = response.json().get("items", [])
    # )
    fetched_news  = []
    for article in articles:
        news_item = FetchedNewsType(
            title=article.get("title"),
            link=article.get("link"),
            domain=article.get("link")  # the domain
        )
        fetched_news.append(news_item)
    
    return fetched_news

    # return response.json().get("items")



# example
# query = "U.S. military to accept transgender recruits on Monday: Pentagon"

# results = google_news_search(query, API_KEY, CSE_ID)

# # Print titles and links
# for result in results:
#     print(f"Link: {result['displayLink']}\n")
#     print(f"Title: {result['title']}")
#     print(f"Link: {result['link']}\n")
#     print(f"Link: {result['snippet']}\n")