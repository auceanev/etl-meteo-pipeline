import logging
from extract import extract_meteo
from transform import transform_meteo
from load import load_meteo, query_exemple

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

def run_pipeline() -> None:
    logger.info("=== Démarrage du pipeline ETL Météo ===")
    try:
        raw = extract_meteo()
        df = transform_meteo(raw)
        load_meteo(df)
        logger.info("=== Pipeline terminé avec succès ===")
        print("\nAperçu des données chargées :")
        print(query_exemple())
    except Exception:
        logger.exception("Erreur dans le pipeline")
        raise

if __name__ == "__main__":
    run_pipeline()