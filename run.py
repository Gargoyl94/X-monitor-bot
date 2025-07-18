import os
from dotenv import load_dotenv
from scraper import fetch_posts
from classifier import classify_posts
from chart_analyzer import analyze_charts
from router import route_to_chats
from alert import send_alerts
from logger import log_entries

def main():
    load_dotenv()
    posts = fetch_posts()
    scored = classify_posts(posts)
    chart_results = analyze_charts([p for p in scored if p["score"] >= 8])
    route_to_chats(scored, chart_results)
    send_alerts(scored, chart_results)
    log_entries(scored, chart_results)

if __name__ == "__main__":
    main()
