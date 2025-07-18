import os
from datetime import datetime, timedelta
# import snscrape.modules.twitter as sntwitter
# import tweepy

ACCOUNTS = [
    "ValueSense_io", "iamJMinx", "astocks92", "AlphaPicks",
    # … deine weiteren Accounts
]

def fetch_posts():
    posts = []
    # Beispiel mit snscrape (auskommentiert):
    # for acc in ACCOUNTS:
    #     since = datetime.utcnow() - timedelta(minutes=10)
    #     query = f"from:{acc} since:{since.date()}"
    #     for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    #         posts.append({
    #             "account": acc,
    #             "post_id": tweet.id,
    #             "text": tweet.content,
    #             "timestamp": tweet.date
    #         })
    return posts
