# X-Monitor-Bot

Automatisches Monitoring deiner X-Posts mit Score, Chart-Analyse & Alerts.

## Setup

1. Fork oder Clone das Repo.
2. `cp .env.example .env` und ENV-Variablen ausfüllen.
3. `pip install -r requirements.txt`
4. `heroku create`
5. `git push heroku main`
6. Heroku Scheduler: `run: python run.py` alle 5 Min.
