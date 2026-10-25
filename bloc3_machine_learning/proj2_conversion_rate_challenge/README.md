# Defi du Taux de Conversion - Data Science Weekly

## Contexte

www.datascienceweekly.org est une newsletter hebdomadaire redigee par des data scientists independants. N'importe qui peut s'inscrire sur le site en indiquant son adresse e-mail pour recevoir chaque semaine des actualites sur la science des donnees.

Les data scientists a l'origine de la newsletter souhaitent mieux comprendre le comportement des visiteurs de leur site. L'objectif est de construire un modele capable de predire si un visiteur va s'abonner a la newsletter, a partir de quelques informations sur son profil et son comportement de navigation.

Ce projet s'inscrit dans le cadre d'une competition de type Kaggle. La metrique imposee pour evaluer les performances est le score F1. Ce choix se justifie par le fort desequilibre des classes du jeu de donnees, rendant une metrique comme l'exactitude (accuracy) trompeuse.

---

## Structure du projet


```

2-defi-du-taux-de-conversion/
│
├── data/
│   ├── conversion_data_train.csv     # Donnees d'entrainement (avec etiquettes)
│   └── conversion_data_test.csv      # Donnees de test (sans etiquettes)
│
├── fs_bloc3_conversion_rate_challenge.ipynb    # Notebook principal
├── predictions_soumission.csv                  # Predictions finales à soumettre
└── README.md                                   

```

---

## Description des donnees

### Jeu d'entrainement : `conversion_data_train.csv`

- Lignes : 284 578 (apres suppression des 2 valeurs aberrantes) x 6 colonnes
- Contient la variable cible : `converted`

### Jeu de test : `conversion_data_test.csv`

- Lignes : 31 620 x 5 colonnes
- Ne contient pas la variable cible (utilise pour generer les predictions finales a soumettre)

### Description des variables

| Variable | Type | Description |
|---|---|---|
| country | Categorielle | Pays du visiteur : China, Germany, UK, US |
| age | Numerique | Age du visiteur (en annees) |
| new_user | Binaire | 1 = nouvel utilisateur, 0 = utilisateur existant |
| source | Categorielle | Source du trafic : Ads, Seo, Direct |
| total_pages_visited | Numerique | Nombre de pages visitees lors de la session |
| converted | Cible (0/1) | 1 = abonne a la newsletter, 0 = non abonne |

---

## Principaux resultats de l'analyse exploratoire (EDA)

### Desequilibre des classes

Le jeu de donnees presente un fort desequilibre :
- Non convertis : 275 400 visiteurs (96,77 %)
- Convertis : 9 178 visiteurs (3,23 %)

### Valeurs aberrantes detectees

La variable `age` contenait deux individus avec des valeurs superieures a 100 ans (dont une valeur a 123 ans), ce qui s'apparente a des erreurs manifestes de saisie. Ces observations representant moins de 0,001 % des donnees, elles ont ete retirees du jeu d'entrainement pour ne pas biaiser l'apprentissage des modeles.

### Correlations avec la variable cible

| Variable | Correlation lineaire |
|---|---|
| total_pages_visited | +0,529 |
| country (encode) | +0,077 |
| age | -0,089 |
| new_user | -0,152 |
| source (encode) | -0,003 |

La variable `total_pages_visited` montre la correlation la plus significative avec l'acte d'abonnement.

### Taux de conversion par segment de pages visitees

| Segment | Taux de conversion |
|---|---|
| 1-3 pages | 0,0 % |
| 4-7 pages | 0,3 % |
| 8-15 pages | 10,9 % |
| 16+ pages | 94,3 % |

### Taux de conversion par variable categorielle

Taux par pays :
- Germany : 6,2 %
- UK : 5,2 %
- US : 3,8 %
- China : 0,1 %

Note methodologique : Le taux de la Chine est anormalement bas. Cela suggere une contrainte d'ordre technique ou reglementaire liee a l'infrastructure web locale plutot qu'un desinteret culturel pour la science des donnees.

Taux par source de trafic :
- Ads : 3,5 %
- Seo : 3,3 %
- Direct : 2,8 %

Taux par statut utilisateur :
- Utilisateur existant (new_user=0) : 7,2 %
- Nouvel utilisateur (new_user=1) : 1,4 %

---

### Performances des modeles sur l'ensemble de validation

| Modèle | Score F1 | Precision | Recall  |
|---|---|---|---|
| XGBoost  |  0.7650  |   0.8084 | 0.7260 |
| Random Forest  |  0.7613   |  0.7830 | 0.7407 |
| Régression logistique  |  0.7604   |  0.8620 | 0.6803 |

### Hyperparametres du meilleur modele (Gradient Boosting)

```python
XGBClassifier(
    n_estimators=200,
    learning_rate=0.01,
    max_depth=7,
    subsample=0.8,
    scale_pos_weight=2
)

```

## Predictions finales

Apres validation, le modele de XGBoost a été re-entraine sur l'integralite du jeu de donnees d'entrainement disponible afin de maximiser la quantite d'information utilisee avant la phase de deploiement.

* Fichier produit : `predictions_soumission.csv`
* Volume de lignes : 31 620

---

## Recommandations metier

1. Augmenter la profondeur des sessions utilisateurs (Priorite haute) : La variable liee au nombre de pages visitees represente plus de 84 % de l'importance du modele. Il convient de developper des fonctionnalites favorisant l'engagement (recommandation d'articles croises, apercus de newsletters precedentes) pour inciter le visiteur a franchir le palier des 8 pages, a partir duquel le taux de conversion augmente drastiquement.
2. Mise en place d'actions de reciblage (Priorite haute) : Les utilisateurs deja enregistres convertissent 5 fois plus que les nouveaux visiteurs (7,2 % contre 1,4 %). Un programme de retargeting par e-mail ou sur les reseaux professionnels est fortement conseille.
3. Campagnes ciblees sur les jeunes actifs et etudiants (Priorite moyenne) : La tranche d'age 18-25 ans affiche les meilleurs resultats de conversion. Les partenariats strategiques avec des plateformes d'apprentissage et des formations specialisees en data science constituent un levier d'acquisition optimal.
4. Audit technique sur la region Chine (Priorite basse) : Le taux de 0,1 % necessite une analyse des temps de chargement du site ou des blocages reseaux potentiels afin de verifier si le produit est correctement accessible sur ce marche.


---
## Stack Technique

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C9BE8?style=for-the-badge&logoColor=white)
