import os
from langchain import OpenAI, ConversationChain

SESSION_MAP = {
    # "AAPL": "session-id-123",
}

def route_to_chats(scored_posts, chart_results):
    llm = OpenAI(temperature=0)
    for p in scored_posts:
        for ticker in p["ticker_list"]:
            session_id = SESSION_MAP.get(ticker)
            if session_id:
                conv = ConversationChain(llm=llm)
                prompt = f"Neuer Post von {p['account']}: {p['text']}\nScore: {p['score']}"
                if p["score"] >= 8:
                    cr = next((c for c in chart_results if c["post_id"] == p["post_id"]), {})
                    prompt += f"\nChart-Analyse: {cr}"
                conv.run(prompt)
