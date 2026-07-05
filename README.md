---
title: Consommation
emoji: 📈
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 6.19.0
app_file: app.py
pinned: false
---

# ⚡ Seattle Energy Prediction API

## Présentation

Ce projet a pour objectif de déployer un modèle de Machine Learning permettant de prédire la consommation énergétique de bâtiments non résidentiels de la ville de Seattle.

L'application expose le modèle via une API REST développée avec **FastAPI** et propose également une interface utilisateur **Gradio**.

Le modèle de Machine Learning est stocké sur **Hugging Face Hub** et téléchargé automatiquement au démarrage de l'application.

Toutes les prédictions sont enregistrées dans une base de données **SQLite** à l'aide de SQLAlchemy.

---

# Technologies utilisées

* Python 3.11
* FastAPI
* Gradio
* Pydantic
* Scikit-learn
* Pandas
* SQLAlchemy
* SQLite
* Hugging Face Hub
* GitHub Actions
* Pytest
* Pytest-cov

---

# Architecture du projet

```text
projet5elec/

├── app/
│   ├── app_gradio.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── ml_model.py
│   ├── models.py
│   ├── schemas.py
│   └── __init__.py
│
├── data/
│   └── energie.ipynb
│
├── scripts/
│
├── tests/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Modèle de Machine Learning

Le modèle prédit :

**SiteEnergyUse(kBtu)**

Variables utilisées :

* YearBuilt
* BuildingAge
* NumberofFloors
* Log_Surface
* PropertyGFATotal
* LargestPropertyUseTypeGFA
* PropertyGFABuilding(s)
* BuildingType
* PrimaryPropertyType
* City
* State

Le modèle est un :

**RandomForestRegressor**

Le fichier `model.pkl` est hébergé sur **Hugging Face Hub** puis téléchargé automatiquement grâce à :

* huggingface_hub
* joblib

---

# Installation

Cloner le dépôt :

```bash
git clone https://github.com/mansour-ndoye/projet5elec.git
cd projet5elec
```

Créer un environnement virtuel :

Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS :

```bash
python -m venv venv
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

# Base de données

Le projet utilise **SQLite**.

La base est créée automatiquement au premier lancement.

Aucune installation supplémentaire n'est nécessaire.

---

# Lancement de l'application

```bash
python app.py
```

ou

```bash
uvicorn app.main:app --reload
```

---

# Documentation de l'API

Swagger :

```text
http://127.0.0.1:8000/docs
```

ReDoc :

```text
http://127.0.0.1:8000/redoc
```

---

# Interface Gradio

Lorsque l'application est déployée sur Hugging Face Spaces, une interface Gradio est disponible en complément de l'API.

Elle permet de réaliser une prédiction directement depuis un navigateur.

---

# Exemple d'appel API

POST `/predict`

```json
{
  "YearBuilt": 1992,
  "BuildingAge": 24,
  "NumberofFloors": 3,
  "Log_Surface": 13.111982,
  "PropertyGFATotal": 494835,
  "LargestPropertyUseTypeGFA": 757027,
  "PropertyGFABuilding_s": 494835,
  "BuildingType": "Campus",
  "PrimaryPropertyType": "Mixed Use Property",
  "City": "Seattle",
  "State": "WA"
}
```

Réponse :

```json
{
  "prediction_kbtu": 71888207.72
}
```

---

# Traçabilité des prédictions

Chaque appel au endpoint `/predict` suit les étapes suivantes :

1. Validation des données avec Pydantic.
2. Création des variables d'entrée.
3. Chargement du modèle Machine Learning.
4. Calcul de la prédiction.
5. Enregistrement de la prédiction dans SQLite.
6. Retour de la réponse au client.

---

# Tests

Lancer tous les tests :

```bash
pytest
```

Couverture :

```bash
pytest --cov=app
```

Tous les tests passent avec succès.

---

# Déploiement CI/CD

Le projet est déployé automatiquement grâce à GitHub Actions et Hugging Face Spaces.

À chaque `git push` :

* les tests sont exécutés automatiquement ;
* le projet est vérifié ;
* Hugging Face redéploie automatiquement la nouvelle version de l'application.

Cette approche met en œuvre une chaîne **CI/CD** garantissant la qualité et la disponibilité du projet.

---

# Déploiement

Le projet est disponible sur :

* API FastAPI
* Documentation Swagger
* Interface Gradio
* Hugging Face Hub pour le stockage du modèle

---

# Auteur

Projet réalisé dans le cadre du parcours **OpenClassrooms – Ingénieur Intelligence Artificielle**.
