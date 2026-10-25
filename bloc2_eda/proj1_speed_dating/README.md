# Speed Dating Analysis - Qu'est-ce qui déclenche l'étincelle ?

Analyse exploratoire des données de l'expérience de speed dating de l'Université Columbia (2002-2004), appliquée à la stratégie produit de Tinder.

## Contexte

L'équipe marketing de Tinder a observé une baisse du nombre de matchs et a commandé cette étude pour comprendre **ce qui attire les gens les uns vers les autres**.
Le dataset couvre **8 378 rencontres** entre participants qui se sont notés sur 6 critères et ont indiqué s'ils souhaitaient un second rendez-vous.

## Dataset

- **Source :** Columbia University Speed Dating Experiment (2002-2004)
- **Lignes :** 8 378 rencontres (une ligne = un speed date entre deux personnes)
- **Colonnes :** 195 variables (démographie, auto-perception, notes, style de vie)
- **Variable cible :** `match` - 1 si les deux ont dit oui (taux moyen : **16,5 %**)

[Download CSV](https://full-stack-assets.s3.eu-west-3.amazonaws.com/M03-EDA/Speed+Dating+Data.csv) | [Data Dictionary](https://full-stack-assets.s3.eu-west-3.amazonaws.com/M03-EDA/Speed+Dating+Data+Key.doc)

## Questions de recherche

- Quels sont les critères les moins désirables chez un partenaire ? Cela diffère-t-il selon le genre ?
- Quelle importance les gens accordent-ils à l'attractivité par rapport à son impact réel ?
- L'origine raciale a-t-elle un grand impact ?
- Les gens peuvent-ils estimer correctement leur valeur perçue sur le marché des rencontres ?
- Vaut-il mieux être le premier ou le dernier speed date de la soirée ?

## Résultats clés

- **L'attractivité domine** : le critère le plus prédictif, pourtant sous-déclaré chez les femmes. Biais de désirabilité sociale confirmé.
- **L'humour et les intérêts communs suivent** : des signaux actionnables pour un algorithme de matching.
- **L'auto-perception est peu fiable** : surestimation de l'attractivité de +0.9 pt, de la sincérité de +1.13 pt.
- **La fatigue décisionnelle se confirme, avec un effet modéré** : le taux d'acceptation décline régulièrement au fil de la soirée.

## Recommandations pour Tinder

1. **Valoriser la photo** - l'attractivité est le premier filtre ; aider les utilisateurs à choisir leur meilleure photo.
2. **Algorithme Passions** - pondérer les tags d'intérêts dans le matching.
3. **Limiter les swipes par session** - lutter contre la fatigue décisionnelle via une limite quotidienne ou des pauses suggérées.
4. **Calibration de profil** - un feedback anonymisé aide les utilisateurs à aligner leurs attentes sur la réalité du marché.

## Structure du projet

```
.
├── fs_bloc2_speed_dating.ipynb          # Notebook d'analyse principal (EDA + visualisations)
├── Bloc2_Prés_Speed_Dating.pdf        # Présentation
└── README.md
```

## Stack Technique

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%2311557c.svg?style=for-the-badge&logo=Matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-%234C72B0.svg?style=for-the-badge&logo=Seaborn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%234C72B0.svg?style=for-the-badge&logo=Plotly&logoColor=white)

---