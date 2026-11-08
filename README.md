# - Prompt Engineering

Projet de classification de sentiment appliqué au dataset **IMDB Movie Reviews** avec des modèles de langage locaux et différentes techniques de prompt engineering.

Le projet compare des stratégies de prompting afin d'évaluer leur capacité à prédire si une critique de film est **positive** ou **négative**.

## Fonctionnalités

- Chargement et exploration du jeu de données IMDB
- Nettoyage et prétraitement des critiques
- Classification avec le modèle local `llama3.2` via Ollama
- Comparaison de quatre techniques de prompting :
  - Zero-shot
  - Few-shot
  - Role-based
  - Structured / JSON
- Calcul des métriques : accuracy, précision, rappel et F1-score
- Sauvegarde des résultats dans `results/metrics/prompting_metrics.csv`

## Structure du projet

```text
.
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_data_exploration.ipynb
├── results/
│   ├── metrics/
│   └── predictions/
├── src/
│   └── prompt_engineering/
│       ├── data_loader.py
│       ├── evaluation.py
│       ├── llm_client.py
│       ├── preprocessing.py
│       └── prompts.py
├── tests/
├── pyproject.toml
└── uv.lock
```

## Prérequis

- Python 3.13 ou supérieur
- [uv](https://docs.astral.sh/uv/) pour la gestion de l'environnement et des dépendances
- [Ollama](https://ollama.com/) pour l'exécution locale du modèle

## Installation

1. Installer les dépendances du projet :

```powershell
uv sync
```

2. Installer et démarrer Ollama.

3. Télécharger le modèle utilisé par le projet :

```powershell
ollama pull llama3.2
```

4. Vérifier que Ollama répond :

```powershell
ollama run llama3.2
```

Tapez une courte phrase, puis quittez la session.

## Utilisation

Lancer Jupyter :

```powershell
uv run jupyter notebook
```

Ouvrir ensuite [notebooks/01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb) et exécuter les cellules dans l'ordre.

Le notebook :

1. charge les données IMDB ;
2. nettoie les critiques ;
3. prépare les échantillons de test ;
4. génère les prédictions via Ollama ;
5. évalue chaque technique de prompting ;
6. sauvegarde les métriques comparatives.

## Techniques de prompting

Les prompts sont définis dans [src/prompt_engineering/prompts.py](src/prompt_engineering/prompts.py).

| Technique | Description |
|---|---|
| Zero-shot | Demande au modèle de classer une critique sans exemple |
| Few-shot | Fournit plusieurs exemples positifs/négatifs avant la classification |
| Role-based | Assigne au modèle le rôle d'expert en analyse de critiques |
| Structured | Demande une réponse JSON contenant uniquement le sentiment |

Les réponses sont normalisées par [src/prompt_engineering/llm_client.py](src/prompt_engineering/llm_client.py).

## Résultats enregistrés

Les métriques obtenues avec le modèle `llama3.2` sont disponibles dans [results/metrics/prompting_metrics.csv](results/metrics/prompting_metrics.csv).

| Technique | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Zero-shot | 0.90 | 1.00 | 0.76 | 0.86 |
| Few-shot | 0.96 | 0.98 | 0.93 | 0.95 |
| Role-based | 0.86 | 1.00 | 0.67 | 0.80 |

Ces résultats servent à comparer la stabilité et la qualité des différentes formulations de prompts sur l'échantillon testé. Ils peuvent varier selon le modèle, les données sélectionnées et la version d'Ollama.

## Tests

Exécuter les tests unitaires :

```powershell
uv run pytest
```
