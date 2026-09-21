import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


USERNAME = "ABHISHEKGORE2305"

URL = f"https://github.com/users/{USERNAME}/contributions"

print(f"Fetching contributions for {USERNAME}...")

response = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
)

response.raise_for_status()

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

days = []

for cell in soup.select(
    "td.ContributionCalendar-day"
):

    date = cell.get("data-date")
    level = cell.get("data-level")

    if date:

        days.append({
            "date": date,
            "level": int(level or 0)
        })


data = {
    "username": USERNAME,
    "updated_at": datetime.utcnow().isoformat(),
    "days": days
}

with open(
    "data/contributions.json",
    "w"
) as f:

    json.dump(
        data,
        f,
        indent=2
    )

print(
    f"Saved {len(days)} contribution days"
)