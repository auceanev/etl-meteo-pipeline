import requests
from datetime import date, timedelta

def extract_meteo(latitude: float = 48.85, longitude: float = 2.35) -> dict:
    """Appelle l'API Open Meteo et retourne les données brutes JSON."""
    end_date = date.today().isoformat()
    start_date = (date.today() - timedelta(days=7)).isoformat()

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,precipitation,windspeed_10m",
        "start_date": start_date,
        "end_date": end_date,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # lève une erreur si status != 200

    print(f"✓ Extraction OK — {len(response.json()['hourly']['time'])} lignes récupérées")
    return response.json()

if __name__ == "__main__":
    data = extract_meteo()
    print(data["hourly"].keys())