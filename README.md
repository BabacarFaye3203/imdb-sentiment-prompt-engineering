# IMDB Sentiment Analysis — Prompt Engineering

Projet de classification de sentiments appliqué au dataset **IMDB Movie Reviews**, utilisant un modèle de langage local (LLM) et différentes techniques de Prompt Engineering.

L'objectif est de comparer plusieurs stratégies de prompting afin d'évaluer leur capacité à classifier automatiquement les critiques de films en deux catégories : **positive** et **negative**.

Le projet intègre également une API REST avec FastAPI, conteneurisée avec Docker, permettant d'exposer le modèle de classification et de communiquer avec Ollama.

## Objectifs du projet

- Explorer et préparer le dataset IMDB Movie Reviews.
- Étudier l'influence des formulations de prompts sur les performances d'un LLM.
- Comparer plusieurs techniques de Prompt Engineering.
- Évaluer les prédictions à l'aide de métriques de classification.
- Déployer une API REST permettant d'effectuer des prédictions.
- Conteneuriser l'application avec Docker et Docker Compose.

## Fonctionnalités

- Chargement et exploration du dataset IMDB.
- Nettoyage et prétraitement des critiques.
- Classification avec le modèle local `llama3.2` via Ollama.
- Comparaison de cinq techniques de prompting :
  - Zero-shot
  - Few-shot
  - Role-based
  - Structured / JSON
  - Advanced prompting
- Évaluation avec Accuracy, Precision, Recall et F1-score.
- Génération et sauvegarde des résultats expérimentaux.
- API REST développée avec FastAPI.
- Documentation interactive avec Swagger UI.
- Déploiement conteneurisé avec Docker et Docker Compose.

## Technologies utilisées

| Catégorie | Technologies |
|---|---|
| Langage | Python 3.13 |
| Gestion des dépendances | uv |
| Data processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| LLM | Llama 3.2 |
| LLM Runtime | Ollama |
| LLM Integration | LangChain, LangChain-Ollama |
| API | FastAPI, Uvicorn |
| Validation | Pydantic |
| Conteneurisation | Docker, Docker Compose |
| Tests | Pytest |
| Visualisation | Matplotlib, Seaborn |

## Architecture du projet

```text
tp3_sma/
│
├── api/
│   └── main.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── results/
│   ├── metrics/
│   └── predictions/
│
├── src/
│   └── prompt_engineering/
│       ├── __init__.py
│       ├── config.py
│       ├── data_loader.py
│       ├── evaluation.py
│       ├── llm_client.py
│       ├── preprocessing.py
│       └── prompts.py
│
├── tests/
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

## Prérequis

- Python 3.13 ou supérieur
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/)
- Docker Desktop
- Git

## Installation et configuration locale

### 1. Cloner le projet

```bash
git clone https://github.com/BabacarFaye3203/imdb-sentiment-prompt-engineering.git
cd tp3_sma
```

### 2. Installer les dépendances

```powershell
uv sync
```

### 3. Installer et démarrer Ollama

Télécharger et installer Ollama depuis :

https://ollama.com/

Télécharger le modèle :

```powershell
ollama pull llama3.2
```

Vérifier les modèles disponibles :

```powershell
ollama list
```

### 4. Vérifier le fonctionnement du modèle

```powershell
ollama run llama3.2
```

Saisir une phrase pour vérifier que le modèle répond correctement, puis quitter la session.

## Exploration et expérimentation

Lancer Jupyter Notebook :

```powershell
uv run jupyter notebook
```

Ouvrir le notebook :

`notebooks/01_data_exploration.ipynb`

Exécuter les cellules dans l'ordre.

Le processus expérimental comprend :

1. Chargement du dataset IMDB.
2. Exploration et analyse de la distribution des sentiments.
3. Nettoyage des critiques et suppression des doublons.
4. Préparation des données d'entraînement et de test.
5. Construction des différentes stratégies de prompting.
6. Génération des prédictions avec Llama 3.2.
7. Évaluation et comparaison des résultats.
8. Sauvegarde des métriques et prédictions.

## Techniques de Prompt Engineering

Les différentes stratégies sont implémentées dans :

`src/prompt_engineering/prompts.py`

| Technique | Description |
|---|---|
| Zero-shot | Classification sans fournir d'exemples au modèle. |
| Few-shot | Fourniture de quelques exemples annotés avant la classification. |
| Role-based | Attribution d'un rôle spécifique au modèle pour orienter son analyse. |
| Structured / JSON | Imposition d'un format JSON structuré pour standardiser les réponses. |
| Advanced | Utilisation d'instructions plus détaillées pour améliorer la qualité des prédictions. |

Les réponses du modèle sont traitées et normalisées dans :

`src/prompt_engineering/llm_client.py`

## Évaluation des performances

Les performances sont évaluées avec les métriques suivantes :

- **Accuracy** : proportion des prédictions correctes.
- **Precision** : proportion des prédictions positives correctes parmi les prédictions positives.
- **Recall** : capacité à identifier les exemples positifs.
- **F1-score** : moyenne harmonique de la précision et du rappel.

### Résultats expérimentaux

Sur un échantillon de validation de 100 critiques :

| Technique | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Zero-shot | 0.82 | 0.9706 | 0.66 | 0.7857 |
| Few-shot | 0.84 | 0.9722 | 0.70 | 0.8140 |
| Role-based | 0.81 | 0.9697 | 0.64 | 0.7711 |
| Structured / JSON | 0.91 | 0.9020 | 0.92 | 0.9109 |
| Advanced | 0.88 | 0.9130 | 0.84 | 0.8750 |

### Évaluation complémentaire

La stratégie Structured / JSON a également été évaluée sur un échantillon de 1 000 critiques de test :

| Métrique | Résultat |
|---|---:|
| Accuracy | 0.94 |
| Precision | 0.9418 |
| Recall | 0.9380 |
| F1-score | 0.9399 |

Ces résultats montrent que le format structuré améliore l'équilibre entre précision et rappel sur les échantillons évalués.

Les résultats peuvent varier selon le modèle utilisé, les données sélectionnées et les paramètres d'inférence.

Les métriques expérimentales sont disponibles dans :

`results/metrics/prompting_metrics.csv`

## API REST — FastAPI

Une API REST a été développée pour exposer le système de classification.

Le point d'entrée est :

`api/main.py`

### Endpoints

| Méthode | Endpoint | Description |
|---|---|---|
| GET | `/health` | Vérification de l'état de l'API. |
| POST | `/predict` | Classification du sentiment d'une critique. |

### Exemple de requête

**POST /predict**

```json
{
  "review": "This movie was absolutely fantastic! The acting was brilliant and the story was amazing."
}
```

### Exemple de réponse

```json
{
  "sentiment": "positive",
  "model": "llama3.2"
}
```

### Documentation interactive

Une fois l'API démarrée, accéder à Swagger UI :

http://localhost:8000/docs

## Docker Deployment

L'application FastAPI est conteneurisée avec Docker. Ollama et le modèle Llama 3.2 restent installés sur la machine hôte.

### Architecture de déploiement

```text
                  Client
                    |
                    v
             Swagger / HTTP
                    |
                    v
          Docker Container
             FastAPI API
              Port 8000
                    |
                    v
          host.docker.internal
              Port 11434
                    |
                    v
             Ollama Runtime
                    |
                    v
                Llama 3.2
```

### Prérequis

- Docker Desktop installé et démarré.
- Ollama installé sur la machine hôte.
- Modèle `llama3.2` téléchargé.
- Ollama accessible depuis le conteneur Docker.

### 1. Vérifier Ollama

```powershell
ollama list
```

### 2. Construire l'image Docker et démarrer l'application

À la racine du projet :

```powershell
docker compose up --build -d
```

### 3. Vérifier le conteneur

```powershell
docker compose ps
```

### 4. Accéder à l'API

- Documentation Swagger : http://localhost:8000/docs
- Health check : http://localhost:8000/health
- Prédiction : POST http://localhost:8000/predict

### 5. Consulter les logs

```powershell
docker compose logs -f api
```

### 6. Arrêter l'application

```powershell
docker compose down
```

### Configuration réseau

Le conteneur utilise l'adresse suivante pour communiquer avec Ollama :

```text
http://host.docker.internal:11434
```

Cette adresse permet au conteneur Docker de joindre le service Ollama exécuté sur la machine hôte.

Les variables d'environnement sont configurées dans `docker-compose.yml` :

```yaml
environment:
  OLLAMA_BASE_URL: http://host.docker.internal:11434
  OLLAMA_MODEL: llama3.2
```

## Tests

Exécuter les tests unitaires :

```powershell
uv run pytest
```

## Améliorations futures

- Élargir les évaluations à plusieurs modèles de langage.
- Étudier l'influence de la température et des paramètres d'inférence.
- Ajouter des mécanismes de validation et de robustesse des réponses JSON.
- Mettre en place des tests automatisés pour les endpoints FastAPI.
- Ajouter une interface utilisateur pour tester les classifications.
- Étudier les performances et la latence de l'API.
- Déployer l'application sur une infrastructure cloud.

## Auteur

**Babacar Faye**

Master Artificial Intelligence & Digital Computing (AIDC)  
Université Sultan Moulay Slimane (USMS)

Projet académique — Prompt Engineering & Sentiment Analysis.
