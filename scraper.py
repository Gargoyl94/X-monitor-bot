# scraper.py
import os
from datetime import datetime, timedelta
import snscrape.modules.twitter as sntwitter

# Deine Accounts (ohne @)
ACCOUNTS = [
    "ValueSense_io","iamJMinx","astocks92","AlphaPicks",
    "mattdaytrades_","kiantrades","linzy_long_hold","Barkworth17",
    "StockPatternPro","stocktalkweekly","kholov23","TheRealNasa00",
    "TradingWarz","LuxAlgo","VolSignals","_Shark_Trading",
    "blondebroker1","Banana3Stocks","JIMROInvest","EliteOptions2",
    "LadeBackk","itsCblast","TrendSpider","Jedi_ant",
    "VolumeLeaders","Jake__Wujastyk","Biotech_SD","BrianHouser11",
    "SethCL","edgaralandough","KochWallStreet","Mayhem4Markets",
    "The_RockTrading","alphatrends","t3live","ShortsellerST"
]

def fetch_posts():
    """
    Liefert eine Liste von Dicts:
    [
      {
        "account": str,
        "post_id": str,
        "text": str,
        "timestamp": datetime
      },
      ...
    ]
    """
    posts = []
    since = datetime.utcnow() - timedelta(minutes=10)
    for acc in ACCOUNTS:
        query = f"from:{acc} since:{since.date()}"
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            # Nur neuere als 'since' aufnehmen
            if tweet.date > since:
                posts.append({
                    "account": acc,
                    "post_id": str(tweet.id),
                    "text": tweet.content,
                    "timestamp": tweet.date
                })
    return posts
