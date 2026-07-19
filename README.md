---
title: Consommation
emoji: 📈
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 5.34.2
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

- Python 3.11
- FastAPI
- Gradio
- Pydantic
- SQLAlchemy
- PostgreSQL (Neon)
- Scikit-learn
- Pandas
- Joblib
- Pytest
- GitHub Actions
- Hugging Face Spaces

---

# Architecture du projet

```text
projet5elec/

│
├── app/
│   ├── app_gradio.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── ml_model.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
│
├── data/
│   └── energie.ipynb
│
├── scripts/
│
├── tests/
│
├── requirements.txt
├── app.py
└── README.md
```
---

# Architecture globale

```
                    Utilisateur
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
   Interface Gradio              API FastAPI
          │                             │
          │                             │
          ▼                             ▼
                Modèle Machine Learning
                         │
                         ▼
              Random Forest Regressor
                         │
                         ▼
             Base PostgreSQL (Neon)
                         │
                         ▼
 Historisation des prédictions + Monitoring
```
---

# Modèle de Machine Learning

Le modèle utilisé est :

**RandomForestRegressor**

Variable cible :

```
SiteEnergyUse(kBtu)
```

Variables utilisées :

- YearBuilt
- BuildingAge
- NumberofFloors
- Log_Surface
- PropertyGFATotal
- LargestPropertyUseTypeGFA
- PropertyGFABuilding_s
- BuildingType
- PrimaryPropertyType
- City
- State

---

# Base de données

Le projet utilise **Neon PostgreSQL**.

Trois tables permettent d'assurer la traçabilité complète.

## predictions

Historique complet des prédictions réalisées.

## monitoring

Temps de réponse du modèle.

Version du modèle.

Statut de la prédiction.

## dataset

Source des données.

Version des données utilisées.

---

# Sécurité

Les endpoints de prédiction sont protégés par une **API Key**.

Chaque requête doit contenir :

```
X-API-Key: votre_api_key
```

L'API Key est stockée dans les variables d'environnement.

---

# Installation

Cloner le dépôt :

```bash
git clone https://github.com/mansour-ndoye/projet5elec.git

cd projet5elec
```

Créer un environnement virtuel :

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux

```bash
python -m venv venv
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

# Variables d'environnement

Créer un fichier `.env`

```
DATABASE_URL=postgresql://...

API_KEY=xxxxxxxx

HF_TOKEN=xxxxxxxx
```

---

# Lancer l'API

```bash
uvicorn app.main:app --reload
```

API disponible :

```
http://127.0.0.1:8000
```

---

# Documentation

Swagger :

```
http://127.0.0.1:8000/docs
```

ReDoc :

```
http://127.0.0.1:8000/redoc
```

---

# Interface Gradio

Accessible directement depuis :

```
http://127.0.0.1:8000/gradio
```

---

# Exemple d'appel API

```
POST /predict
```

Header

```
X-API-Key: votre_api_key
```

Body

```json
{
  "YearBuilt": 2005,
  "BuildingAge": 21,
  "NumberofFloors": 5,
  "Log_Surface": 11,
  "PropertyGFATotal": 100000,
  "LargestPropertyUseTypeGFA": 80000,
  "PropertyGFABuilding_s": 95000,
  "BuildingType": "NonResidential",
  "PrimaryPropertyType": "Office",
  "City": "Seattle",
  "State": "WA"
}
```

Réponse

```json
{
    "prediction_kbtu": 123456.78
}
```

---

# Tests

Lancer les tests

```bash
pytest
```

Couverture

```bash
pytest --cov=app
```

---

# Git

Le projet suit une stratégie de branches :

- master
- dev
- feature/database
- feature/api
- feature/model
- feature/tests
- feature/cicd

Les versions sont identifiées par des **tags Git**.

Exemple :

```
v1.0
v1.1
```

---

# CI/CD

GitHub Actions permet automatiquement :

- exécution des tests
- vérification du code
- déploiement sur Hugging Face Spaces

---

# Déploiement

Le projet est déployé automatiquement sur **Hugging Face Spaces** après validation des tests GitHub Actions.

---

# Auteur

Projet réalisé dans le cadre de la formation

**OpenClassrooms – Ingénieur Intelligence Artificielle**