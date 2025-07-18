import re
import openai
from dotenv import load_dotenv
load_dotenv()

def extract_ticker(text):
    matches = re.findall(r"\$[A-Z]{1,5}", text)
    return [m.strip("$") for m in matches]

def classify_posts(posts):
    results = []
    for p in posts:
        tickers = extract_ticker(p["text"])
        score = 0.0  # TODO: Implementiere Bewertungslogik
        results.append({**p, "ticker_list": tickers, "score": score})
    return results
