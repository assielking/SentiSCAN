# Analyse de Sentiments avec FastAPI et Scikit-Learn

Ce projet utilise FastAPI pour créer une API Web qui effectue une analyse de sentiments sur les commentaires YouTube en utilisant un modèle de machine learning basé sur Scikit-Learn. L'objectif principal est de classifier les commentaires en sentiments positifs, négatifs ou neutres et d'autres classes encore.

## Prérequis

Assurez-vous d'avoir les dépendances suivantes installées pour exécuter ce projet :
- Python (version recommandée : 3.8+)
- FastAPI (version recommandée : 0.68+)
- Pydantic (version recommandée : 1.9+)
- Scikit-Learn (version recommandée : 1.2.2)
- Uvicorn (pour exécuter le serveur FastAPI)

Installez ces dépendances en utilisant les commandes suivantes :

```bash
conda install scikit-learn=1.2.2
pip install fastapi --upgrade
pip install pydantic --upgrade
