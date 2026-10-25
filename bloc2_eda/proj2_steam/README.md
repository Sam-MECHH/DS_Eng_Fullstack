# Projet Steam - Analyse exploratoire de la plateforme de jeux vidéo

## Contexte

Analyse exploratoire complète (EDA) des jeux disponibles sur Steam, réalisée pour le compte d'**Ubisoft** afin d'orienter la stratégie de lancement d'un nouveau jeu vidéo.

---

## Dataset

| Propriété | Valeur |
|-----------|--------|
| Source | AWS S3 |
| URL | `s3://full-stack-bigdata-datasets/Big_Data/Project_Steam/steam_game_output.json` |
| Format | JSON semi-structuré (schéma imbriqué) |
| Volume | 55 690 jeux après filtrage |

---

## Stack technique

`PySpark 4.2` - `Databricks Free Edition` - `AWS S3`

---

## Structure du projet

```
./
├── fs_bloc2_steam.ipynb       - Notebook Databricks : EDA
├── fs_bloc2_steam.html        - Notebook au format .html pour les visualisations intéractives.
├── images/                    - Captures Databricks
```

## Résultats clés

### Macro
| Indicateur | Résultat |
|------------|----------|
| Éditeur le plus prolifique | Big Fish Games - 422 jeux |
| Ubisoft | 9ème éditeur - 127 jeux |
| Année record | 2021 - 8 823 sorties |
| Langue dominante | English - 55 116 jeux |
| Jeux tous publics | 98.8% des jeux |

### Genres
| Indicateur | Résultat |
|------------|----------|
| Genre le plus représenté | Indie - 39 681 jeux (marché saturé) |
| Genre le plus lucratif | Action - 5 milliards $ |
| Meilleur ratio d'avis | Action, Adventure, RPG - 74% |

### Plateformes
| Plateforme | Part du marché |
|------------|---------------|
| Windows | environ 100% |
| Mac | 23% |
| Linux | 15% |

---

## Recommandations pour Ubisoft

- **Genre** : Action / Adventure - le plus lucratif
- **Plateforme** : Windows en priorité, Mac recommandé pour se différencier
- **Prix** : Entre 10 et 20 euros - zone optimale du marché
- **Langues** : EN + DE + FR + RU

## Stack technique

![PySpark](https://img.shields.io/badge/PySpark-E25A1B?style=for-the-badge&logo=apache-spark&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
