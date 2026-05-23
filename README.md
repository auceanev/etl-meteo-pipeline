# ETL Météo Pipeline

Pipeline ETL Python qui extrait les données météo horaires de Paris
via l'API Open Meteo, les transforme et les stocke dans une base SQLite.

## Architecture

API Open Meteo → extract.py → transform.py → load.py → SQLite

## Stack

- Python 3.x
- pandas
- requests
- SQLite

## Installation

```bash
git clone git@github.com:auceanev/etl-meteo-pipeline.git
cd etl-meteo-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Utilisation

```bash
python pipeline.py
```
---
## Structure
```
etl_meteo/
├── extract.py      # Appel API Open Meteo
├── transform.py    # Nettoyage et enrichissement pandas
├── load.py         # Stockage SQLite
├── pipeline.py     # Orchestrateur ETL
└── requirements.txt
```
---
## Données collectées

- Température horaire (°C)
- Précipitations (mm)
- Vitesse du vent (km/h)
- Période : 7 derniers jours, mise à jour toutes les heures