import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("meteo.db")

def load_meteo(df: pd.DataFrame) -> None:
    """Charge le DataFrame dans une table SQLite."""
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(
            name="meteo_paris",
            con=conn,
            if_exists="replace",   # remplace à chaque run
            index=False,
        )
    print(f"✓ Chargement OK — {len(df)} lignes dans '{DB_PATH}' (table meteo_paris)")

def query_exemple(sql: str = "SELECT date, AVG(temperature_c) as temp_moy FROM meteo_paris GROUP BY date") -> pd.DataFrame:
    """Exemple de requête pour vérifier le contenu."""
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql(sql, conn)

if __name__ == "__main__":
    from extract import extract_meteo
    from transform import transform_meteo
    df = transform_meteo(extract_meteo())
    load_meteo(df)
    print(query_exemple())