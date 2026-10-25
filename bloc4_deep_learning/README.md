# AT&T Spam Detector - Detection de SMS frauduleux par Deep Learning

## Presentation du projet
Ce projet consiste a developper un outil de classification de texte automatise et scalable pour AT&T Inc., leader mondial des telecommunications. L'objectif est d'identifier et de filtrer en temps reel les messages indesarables (spams/phishing) des leur reception afin de securiser les utilisateurs et de soulager le processus de signalement manuel.

Le projet met en concurrence deux approches d'apprentissage profond (Deep Learning) appliquees au Traitement du Langage Naturel (NLP) : une architecture personnalisée et une approche par transfert d'apprentissage.

---

## Jeu de donnees
Le modèle est entrainé sur un corpus de 5 572 messages bruts (reduits a 5 169 exemples uniques apres elimination des doublons).
* Repartition initiale : 87,37 % de messages legitimes (Ham) et 12,63 % de messages frauduleux (Spam).
* Pretraitement : tokenisation, application d'un decoupage stratifié (Train 80% / Test 20%) pour maintenir la proportion de spams, et mise en correspondance des longueurs par rembourrage (padding).

---

## Modeles et approches de Deep Learning

1. Modele 1 - Architecture sur-mesure (Embedding + MLP)
   * Principe : Une couche d'apprentissage d'incorporation de mots (Embedding Layer) pour capter le vocabulaire propre aux SMS, couplée à un MLP.
   * Avantage : Infrastructure légère, temps d'entrainement réduit, vitesse d'inference très rapide, ideal pour un deploiement sur serveurs de production standards sans GPU obligatoire.

2. Modele 2/3 - Transfert d'Apprentissage BERTs (DistilBERT/RoBERTa)
   * Principe : Utilisation d modèles de langage pre-entrainés (issus de la bibliotheque Transformers d'Hugging Face) avec ajout d'une tête de classification dédiée. Les modèles sont affinés (fine-tuned) sur notre base de SMS.
   * Avantage : Compréhension sémantique et contextuelle extremement poussée du langage humain, maximisant le pouvoir de discrimination.

---

## Résultats et Performances

Les performances mesurées sur le jeu de test independant (1 034 messages) revelent d'excellents scores :

|Modèle | Recall | Precision | F1_score |
|---|---|---|---|                               
Baseline | 0.90|        0.91 |      0.91| 
DistilBERT   |  0.95     |   0.98  |     0.97| 
RoBERTa   |     0.98    |    0.97    |   0.97| 

Le choix entre les modèles dépend des contraintes opérationnelles d'AT&T :
- Priorité à la **vitesse d'inférence** et à la **légèreté** : DistilBERT ou Embedding + MLP.
- Priorité à la **performance**: RoBERTa ou DistilBERT.

---

## Stack Technique

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Transformers-Hugging%20Face-FFD21E?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
