# Energie API

API de prédiction de consommation énergétique des bâtiments de Seattle.

## Objectif

Déployer un modèle de Machine Learning avec FastAPI afin de prédire la consommation énergétique des bâtiments non résidentiels.

## Technologies utilisées

* Python
* FastAPI
* Scikit-learn
* PostgreSQL
* SQLAlchemy
* Pytest
* GitHub Actions

## Installation

```bash
git clone <repo>
cd energie-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Lancer l’API

```bash
uvicorn app.main:app --reload
```

## Documentation API

Swagger :

```text
http://127.0.0.1:8000/docs
```

## Tests

```bash
pytest
```

