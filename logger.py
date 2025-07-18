from datetime import datetime

def log_entries(scored_posts, chart_results):
    for p in scored_posts:
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "account": p["account"],
            "post_id": p["post_id"],
            "tickers": p["ticker_list"],
            "score": p["score"],
            "metrics": next((c["metrics"] for c in chart_results if c["post_id"] == p["post_id"]), {})
        }
        print("LOG:", entry)
