# Plan your trip with Kayak

Pipeline ETL complet qui recommande les **5 meilleures destinations** et les **20 meilleurs hôtels** en France, en combinant des données météorologiques et hôtelières collectées automatiquement, puis stockées dans une architecture Data Lake / Data Warehouse.

## Contexte et objectif

L'équipe marketing souhaite un outil de recommandation de destinations fondé sur des données réelles. Aucune base n'existant au départ, le projet collecte, nettoie, stocke et restitue les données de bout en bout :

- coordonnées géographiques des villes,
- prévisions météorologiques,
- offre hôtelière (nom, note, lien, description).

Le périmètre couvre les 35 villes françaises imposées par le cahier des charges.

## Sources de données

| Source | Usage | Accès |
|---|---|---|
| Nominatim (OpenStreetMap) | Coordonnées GPS des villes et des hôtels | Gratuit, sans clé |
| OpenWeatherMap (endpoint forecast 5 j / 3 h) | Température, probabilité et volume de pluie | Clé API gratuite |
| Booking.com | Hôtels : nom, note, lien, description | Scraping Selenium |

## Structure du dépôt

```
Projet-Planifiez votre voyage avec Kayak/
├── README.md
├── fs_bloc1_kayak.ipynb
├── data/
│   ├── villes_gps.csv
│   ├── villes_meteo_previsions.csv
│   ├── villes_booking_hotels.csv
│   ├── villes_raw_data.csv
│   ├── kayak_final_enriched_data.csv
├── images/
│   ├── Top5_destinations.png
│   ├── Top20_hôtels_les_mieux_notés.png
│   ├── AWS_S3_bucket.png
│   ├── AWS_RedShift_1.png
│   └── AWS_RedShift_2.png
└── Bloc1_Prés_Kayak.pdf
```

## Méthodologie

**Géocodage.** Nominatim convertit chaque nom de ville (et chaque hôtel) en coordonnées GPS, avec une pause d'une seconde par requête pour respecter la limite du service.

**Météo.** L'endpoint gratuit `forecast` renvoie des prévisions sur 5 jours par pas de 3 heures. Plutôt que de retenir un seul créneau, on **agrège l'ensemble de l'horizon** : température moyenne, probabilité de pluie moyenne et volume de pluie cumulé. L'API One Call sur 7 jours étant devenue payante (moyen de paiement requis), ce choix maintient un coût nul tout en répondant à l'exigence du livrable.

**Scraping.** Booking.com chargeant son contenu en JavaScript, `requests` ne suffit pas : Selenium pilote un navigateur Chrome headless, avec défilement progressif pour déclencher le chargement différé et un checkpoint CSV après chaque ville.

**Nettoyage.** Suppression des hôtels sans note, déduplication par couple (nom, ville), et complétion des descriptions manquantes.

## Score de voyage

Chaque critère est noté sur 10, puis pondéré :

```
travel_score = 4 x pluie + 3 x soleil + 2 x température + 1 x vent
```

Cette approche évite de mélanger des unités différentes (degrés, notes) et rend la pondération transparente et ajustable.

## Stockage

- **Data Lake (AWS S3) :** un csv contenant les données collectées brutes.
- **Data Warehouse (AWS Redshift) :** une database contenant la table finale nettoyée et enrichie.

## Visualisations

Deux cartes interactives Plotly Express:

- **Top 5 destinations**
- **Top 20 hôtels**

## Conformité au RGPD

Le projet ne collecte aucune donnée personnelle de personne physique. Les données sont publiques et non nominatives (villes, météo, fiches d'établissements). Les principes appliqués : minimisation des champs collectés, protection des clés et identifiants via des fichiers `.env` non versionnés, cadences d'appel raisonnables, et accès restreint à l'infrastructure de stockage.

## Stack Technique

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-%23316192.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

