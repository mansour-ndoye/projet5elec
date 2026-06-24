# Seattle Energy Prediction API

## Présentation

Ce projet a pour objectif de déployer un modèle de Machine Learning permettant de prédire la consommation énergétique de bâtiments non résidentiels de la ville de Seattle.

L'application expose le modèle via une API REST développée avec FastAPI. Toutes les prédictions sont enregistrées dans une base de données PostgreSQL afin d'assurer la traçabilité des échanges entre l'API et le modèle.

---

## Technologies utilisées

* Python 3.13
* FastAPI
* Pydantic
* Scikit-learn
* Pandas
* PostgreSQL
* SQLAlchemy
* Pytest
* Pytest-cov
* GitHub Actions

---

## Architecture du projet

```text
projet5elec/

├── app/
│   ├── app_gradio.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── ml_model.py
│   ├── models.py
│   └── schemas.py
│
├── data/
│   ├── energie.ipynb
│   └── model.pkl
│
├── scripts/
│   ├── create_db.py
│   └── load_dataset.py
│
├── tests/
│   ├── test_api.py
│   ├── test_database.py
│   └── test_model.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Modèle de Machine Learning

Le modèle a été entraîné afin de prédire la variable cible :

SiteEnergyUse(kBtu)

Variables utilisées :

YearBuilt
BuildingAge
NumberofFloors
Log_Surface
PropertyGFATotal
LargestPropertyUseTypeGFA
PropertyGFABuilding(s)
BuildingType
PrimaryPropertyType
City
State

### Modèle utilisé

* RandomForestRegressor

### Variables d'entrée

* GHGEmissionsIntensity
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

### Variable cible

* Consommation énergétique du bâtiment (kBtu)

---

## Installation
Cloner le dépôt :

git clone https://github.com/mansour-ndoye/projet5elec.git

cd projet5elec

Créer un environnement virtuel :

python -m venv venv

Activer l'environnement :

Windows :
venv\Scripts\activate

Installer les dépendances :

pip install -r requirements.txt

### Cloner le dépôt

```bash
git clone https://github.com/mansour-ndoye/projet5elec.git
cd projet5elec
```

### Créer un environnement virtuel

Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac :

```bash
python -m venv venv
source venv/bin/activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Configuration PostgreSQL

Créer une base de données PostgreSQL :

```sql
CREATE DATABASE energie_db;
```

Configurer les variables de connexion dans le fichier `.env`.

Exemple :

```env
DATABASE_URL=postgresql://postgres:password@localhost/energie_db
```

---

## Création des tables

Exécuter :

```bash
python -m scripts.create_db
```

Cette commande crée automatiquement les tables définies dans les modèles SQLAlchemy.

---

## Lancement de l'API

```bash
uvicorn app.main:app --reload
```

API disponible sur :

```
http://127.0.0.1:8000
```

---

## Documentation de l'API

Swagger UI :

```

http://127.0.0.1:8000/docs
```

Documentation OpenAPI :

```
http://127.0.0.1:8000/redoc
```

---

## Exemple d'utilisation

### Requête

POST `/predict`

```json
{
  "GHGEmissionsIntensity": 4.0,
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

### Réponse

```json
{
  "prediction_kbtu": 123456.78
}
```

---

## Traçabilité des prédictions

Chaque appel à l'endpoint `/predict` suit le processus suivant :

1. Réception et validation des données via Pydantic.
2. Enregistrement des données d'entrée dans PostgreSQL.
3. Exécution de la prédiction via le modèle Machine Learning.
4. Enregistrement de la prédiction dans PostgreSQL.
5. Retour de la prédiction à l'utilisateur.

Cette approche garantit une traçabilité complète des échanges.

---

## Tests

### Exécuter tous les tests

```bash
pytest -v
```

### Rapport de couverture

```bash
pytest --cov=app
```

Résultat obtenu :

```text
TOTAL 77 0 100%
```

---

## Intégration Continue CI/CD

Le projet utilise GitHub Actions pour :

* exécuter automatiquement les tests ;
* vérifier la qualité du code ;
* garantir la stabilité du projet à chaque modification.

---

## Maintenance du modèle

Pour mettre à jour le modèle :

1. Réentraîner le modèle à partir du notebook d'entraînement.
2. Générer un nouveau fichier `model.pkl`.
3. Remplacer le fichier dans le dossier `data/`.
4. Exécuter la suite de tests.
5. Déployer la nouvelle version.

---

## Auteur

Projet réalisé dans le cadre du parcours OpenClassrooms - Ingénieur Intelligence Artificielle.

