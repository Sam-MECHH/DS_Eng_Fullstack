# Walmart - Prédiction des ventes hebdomadaires

## Présentation

Ce projet construit un modèle de machine learning capable de prédire les ventes hebdomadaires des magasins Walmart à partir d'indicateurs économiques tels que le prix du carburant, le taux de chômage, l'IPC et la température. L'objectif est d'aider l'équipe marketing de Walmart à mieux comprendre les facteurs qui influencent les ventes et à planifier ses futures campagnes.

---

## Structure du projet

Le projet est divisé en trois parties :

- **Partie 1** - Analyse exploratoire des données (EDA) et prétraitement
- **Partie 2** - Régression linéaire (modèle de référence)
- **Partie 3** - Régressions régularisées (Ridge et Lasso) pour réduire le surapprentissage

---

## Jeu de données

Le jeu de données contient les ventes hebdomadaires de plusieurs magasins Walmart ainsi que les variables suivantes :

| Colonne | Description |
|---------|-------------|
| Store | Identifiant du magasin |
| Date | Semaine concernée |
| Weekly_Sales | Variable cible - ventes hebdomadaires en dollars |
| Holiday_Flag | Indique si la semaine contient un jour férié |
| Temperature | Température moyenne dans la région |
| Fuel_Price | Prix du carburant dans la région |
| CPI | Indice des prix à la consommation (IPC) |
| Unemployment | Taux de chômage dans la région |

Volume : 150 observations au départ, 109 après nettoyage (suppression des cibles manquantes puis retrait des valeurs aberrantes).


## Méthodologie

### Partie 1 - EDA et prétraitement

L'exploration des données comprend l'analyse des distributions, l'évolution temporelle des ventes, la comparaison par magasin et une matrice de corrélation.

- Les lignes où `Weekly_Sales` est manquant sont supprimées (aucune imputation sur la variable cible).
- La colonne `Date` est décomposée en features numériques : `Year`, `Month` et `Day`. La feature `DayOfWeek` est écartée car constante (toutes les observations sont des vendredis, variance nulle).

Pipeline de prétraitement construit avec [scikit-learn](https://scikit-learn.org/) :

- Les variables catégorielles (`Store`, `Holiday_Flag`, `Month`) sont encodées avec `OneHotEncoder` (`drop='first'` pour éviter la colinéarité).
- Les variables numériques sont imputées et normalisées avec `SimpleImputer et StandardScaler` : `Temperature`, `Fuel_Price`, `CPI`, `Unemployment`, `Year`.

### Partie 2 - Régression linéaire

Un modèle `LinearRegression` est entraîné dans un pipeline [scikit-learn](https://scikit-learn.org/). Les performances sont évaluées sur les ensembles d'entraînement et de test via R², MAE et RMSE. Les coefficients sont extraits via l'attribut `.coef_` afin d'identifier les variables les plus importantes.

### Partie 3 - Régression régularisée

Les modèles `Ridge` (pénalité L2) et `Lasso` (pénalité L1) sont entraînés pour réduire le surapprentissage. Le paramètre `alpha` est optimisé pour chaque modèle via `GridSearchCV` avec une validation croisée à 5 plis.

---

## Résultats

| Modele | R2 Train | R2 Test | MAE Test ($) | RMSE Test ($) | Ecart R2 Train-Test |
|--------|----------|---------|----------|-----------|-----------------|
|Lin. Regression |  0.9841 | 0.9742  |     87,636  |     106,779  |         0.0099
| Ridge (a=0.01) |  0.9841 | 0.9757  |     83,709  |     103,738  |         0.0084
| Lasso (a=1000) |  0.9818 | 0.9768  |     76,396  |     101,263  |         0.0050


Le modèle Lasso obtient la meilleure performance en terme de réduction des erreurs et éffectue une sélection de variables en annulant les coefficients les moins pertinents (ici 8 coefficients sur 36).

---

## Conclusions principales

- L'identifiant du magasin est de loin le facteur le plus déterminant sur les ventes avec la Date(Month et Year).
- Les ventes affichent une tendance saisonnière.
- Les semaines avec jours fériés génèrent en moyenne 7,5 % de ventes supplémentaires.

---

## Implications pour le service marketing

- Concentrer les budgets promotionnels sur ces périodes ; planifier les campagnes en avance 
- Renforcer les offres de fidélisation et les promotions défensives lors des phases d'inflation
- Adapter la stratégie promotionnelle par zone géographique ; intensifier les offres dans les bassins d'emploi fragilisés

> Aucun indicateur n'agit seul. Le modèle capture leur influence combinée : une campagne optimale devra croiser ces signaux simultanément.

---

## Limites et perspectives

**Limites :**

- Jeu de données réduit (109 observations après nettoyage) : les métriques sont indicatives et demandent confirmation sur un volume plus important.
- La régression linéaire suppose une relation linéaire entre les variables explicatives et la cible.

**Perspectives :**

- Tester des modèles non linéaires (Random Forest, gradient boosting).
- Enrichir le jeu de données avec des sources externes (météo, évènements locaux).
- Industrialiser le modèle via une API de prédiction et un suivi de la dérive en production.

---

## Références

- [scikit-learn - LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [scikit-learn - Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
- [scikit-learn - Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)
- [scikit-learn - GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

---

## Stack technique

![Python](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/SCIKIT_LEARN-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/PANDAS-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NUMPY-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Seaborn](https://img.shields.io/badge/SEABORN-4479A1?style=for-the-badge&logo=データ&logoColor=white)

---
