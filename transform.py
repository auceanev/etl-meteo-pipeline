import pandas as pd

def transform_meteo(raw: dict) -> pd.DataFrame:
    """Transforme le JSON brut en DataFrame nettoyé."""
    hourly = raw["hourly"]
    meta = raw.get("hourly_units", {})

    df = pd.DataFrame({
        "timestamp": pd.to_datetime(hourly["time"]),
        "temperature_c": hourly["temperature_2m"],
        "precipitation_mm": hourly["precipitation"],
        "windspeed_kmh": hourly["windspeed_10m"],
    })

    # Nettoyage
    df = df.dropna()
    df["date"] = df["timestamp"].dt.date
    df["heure"] = df["timestamp"].dt.hour

    # Colonne enrichie : ressenti simplifié
    df["ressenti"] = pd.cut(
        df["temperature_c"],
        bins=[-50, 0, 10, 20, 30, 60],
        labels=["Glacial", "Froid", "Frais", "Agréable", "Chaud"]
    )

    print(f"✓ Transformation OK — {len(df)} lignes, {df['date'].nunique()} jours")
    return df

if __name__ == "__main__":
    from extract import extract_meteo
    raw = extract_meteo()
    df = transform_meteo(raw)
    print(df.head())
    print(df.dtypes)