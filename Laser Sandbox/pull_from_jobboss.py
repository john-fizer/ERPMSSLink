import requests
import pandas as pd
from config import JOBBOSS_API_URL, FIELDS

HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer YOUR_API_TOKEN"
}

def pull_order_line_items():
    response = requests.get(
        JOBBOSS_API_URL,
        headers=HEADERS,
        params={"fields": FIELDS},
        timeout=30
    )
    response.raise_for_status()

    data = response.json()
    records = data.get("items", data)

    return pd.DataFrame(records)
