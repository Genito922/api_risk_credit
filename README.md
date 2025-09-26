# 🏦 Risk Credit – API & SDK Python

[![PyPI version](https://img.shields.io/pypi/v/bankingsdk.svg)](https://pypi.org/project/bankingsdk/)
[![Python versions](https://img.shields.io/pypi/pyversions/bankingsdk.svg)](https://pypi.org/project/bankingsdk/)
[![Build Status](https://github.com/genito92/risk_credit/actions/workflows/tests.yml/badge.svg)](https://github.com/genito92/risk_credit/actions)
[![License](https://img.shields.io/github/license/genito92/risk_credit)](LICENSE)
[![Coverage](https://img.shields.io/codecov/c/github/genito92/risk_credit)](https://codecov.io/gh/genito92/risk_credit)

---

## 📌 Présentation

**Risk Credit** est une solution complète pour :
- ⚡ **API REST (FastAPI)** pour gérer les demandes de crédit, agences, clients.  
- 📦 **SDK Python (`bankingsdk`)** pour interagir facilement avec l’API dans vos projets ML/Data Science.  

👉 Utilisable aussi bien pour les intégrations bancaires que pour les projets de scoring de crédit.

---

## 🚀 Installation

### Installer le SDK depuis **PyPI**

```bash
pip install bankingsdk


## Cloner et lancer le projet complet (API + SDK) ##

git clone https://github.com/genito92/api_risk_credit.git
cd api_risk_credit


## Créer et activer un environnement virtuel ##

python -m venv .venv
source .venv/bin/activate   # sous Linux/Mac
.venv\Scripts\activate      # sous Windows


## Installer les dépendances ##

pip install -r requirements.txt

## Lancer l’API en local ##

uvicorn api_risk_credit.main:app --reload

## Configuration de base ##

from bankingsdk import DemandeClient, BankConfig

# Configurer l’URL de l’API (local ou Render)
config = BankConfig(base_url="https://api-risk-credit.onrender.com")

# Créer un client
client = DemandeClient(config)

## 📊 Arborescence du projet ##

risk_credit/
│── api_risk_credit/       # API FastAPI
│   ├── api/
    │   ├── credit_risk.db # base de donnée sqlite3
    │   ├── database.py
        ├── main.py
        ├── models.py
        ├── query_helpers.py
        ├── schemas.py
        ├── requirements.txt 
    ├── data/              # Liste des fichiers .csv nettoyé et intégré avec des nouvelles données 
        ├── agence_clean.csv
        ├── apport_clean.csv
        ├── demandes_clean.csv
        ├── situation_famille_clean.csv
        ├── situation_pro_clean.csv


    │
    │── sdk/                  # SDK Python (bankingsdk)
    │   ├── bank_client.py
    │   ├── bank_config.py
    │   └── schemas/

    │── requirements.txt
    │── README.md
    │── test_sdk.py / pyproject.toml  # Tests unitaires

