import os
from telegram import Bot
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_alerts(scored_posts, chart_results):
    for p in scored_posts:
        if p["score"] >= 8.5:
            bot.send_message(CHAT_ID, f"🚀 TRADE-READY: {p['ticker_list']} Score {p['score']:.1f}")
        elif p["score"] >= 8.0:
            bot.send_message(CHAT_ID, f"📊 CHART-READY: {p['ticker_list']} Score {p['score']:.1f}")
