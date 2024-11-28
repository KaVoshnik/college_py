import requests

API_URL = "https://openexchangerates.org/api/latest.json"
API_KEY = "359a6d20130a4e3b9cd5eb9133b0ea95"

def fetch_exchange_rates(base_currency: str = "USD") -> dict:
     try:
        response = requests.get(
            API_URL,
            params={"app_id": API_KEY, "base": base_currency}
        )
        response.raise_for_status()
        data = response.json()
        return data["rates"]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except Exception as err:
        print(f"Error: {err}")