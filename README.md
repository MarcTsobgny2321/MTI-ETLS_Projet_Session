# ♻️ Projet BI – Économie Circulaire

## 🎯 ETL (Extraction, Transformation, Loading) - Projet de Session MTI

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-blue.svg)](https://www.mysql.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3+-green.svg)](https://pandas.pydata.org/)

## 📘 Description

Ce projet implémente un pipeline ETL complet pour l'analyse de données liées à l'économie circulaire et à la gestion des matières réutilisables. Il permet l'extraction, la transformation et le chargement de données depuis des fichiers CSV vers une base de données MySQL.

## 🔧 Fonctionnalités

- **Extraction** : Lecture de données depuis des fichiers CSV
- **Transformation** : Nettoyage, validation et préparation des données
- **Chargement** : Insertion des données dans une base MySQL
- **Visualisation** : Graphiques et analyses statistiques
- **Sécurité** : Gestion sécurisée des credentials via variables d'environnement

## 📁 Structure du Projet

```
MTI/
├── ETL_Economie_Circulaire.ipynb    # Notebook principal ETL
├── index.ipynb                      # Notebook d'index/navigation
├── donnees.csv                      # Fichier de données source
├── requirements.txt                 # Dépendances essentielles
├── requirements-full.txt            # Toutes les dépendances
├── .env                            # Variables d'environnement (non versionné)
├── .gitignore                      # Fichiers à ignorer par Git
└── README.md                       # Documentation du projet
```

## 🚀 Installation et Configuration

### 1. Cloner le Repository

```bash
git clone https://github.com/MarcTsobgny2321/MTI-ETLS_Projet_Session.git
cd MTI-ETLS_Projet_Session
```

### 2. Créer un Environnement Virtuel

```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement (Linux/Mac)
source venv/bin/activate

# Activer l'environnement (Windows)
venv\Scripts\activate
```

### 3. Installer les Dépendances

```bash
# Installation minimale (recommandée)
pip install -r requirements.txt

# Ou installation complète
pip install -r requirements-full.txt
```

### 4. Configuration de la Base de Données

#### Option A: MySQL (Recommandée pour production)

1. Installer et démarrer MySQL
2. Créer une base de données :

```sql
CREATE DATABASE `mti-etl`;
```

3. Créer le fichier `.env` :

```bash
# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=mti-etl
DB_TYPE=mysql
```

#### Option B: SQLite (Pour développement rapide)

```bash
# Dans le fichier .env
DB_TYPE=sqlite
SQLITE_PATH=mti-etl.db
```

### 5. Lancer Jupyter

```bash
jupyter notebook
```

## 📊 Utilisation

### 1. Préparation des Données

Placez votre fichier CSV dans le répertoire du projet et nommez-le `donnees.csv`, ou modifiez le chemin dans le notebook.

### 2. Exécution du Pipeline ETL

1. Ouvrir `ETL_Economie_Circulaire.ipynb`
2. Exécuter les cellules dans l'ordre :
   - Installation des dépendances
   - Importation des librairies
   - Extraction des données CSV
   - Transformation et nettoyage
   - Visualisation (optionnel)
   - Chargement en base de données

### 3. Structure des Données Attendues

Le fichier CSV doit contenir au minimum les colonnes :

- `date` : Date au format YYYY-MM-DD
- `type_matiere` : Type de matière recyclable
- `volume_tonnes` : Volume en tonnes
- Autres colonnes selon vos besoins

## 🛠️ Technologies Utilisées

### Backend & Données

- **Python 3.12+** : Langage principal
- **Pandas 2.3+** : Manipulation de données
- **NumPy 2.3+** : Calculs numériques
- **SQLAlchemy 2.0+** : ORM pour bases de données

### Base de Données

- **MySQL 8.0+** : Base de données principale
- **SQLite** : Alternative pour développement

### Visualisation

- **Matplotlib 3.10+** : Graphiques de base
- **Seaborn 0.13+** : Visualisations statistiques

### Environnement de Développement

- **Jupyter Notebook** : Interface interactive
- **python-dotenv** : Gestion des variables d'environnement

## 🔒 Sécurité

- ✅ Credentials stockés dans `.env` (non versionné)
- ✅ `.gitignore` configuré pour exclure les fichiers sensibles
- ✅ Gestion d'erreurs pour les connexions DB
- ✅ Validation des données avant insertion

## 📈 Développement

### Ajouter de Nouvelles Fonctionnalités

1. Créer une nouvelle branche :

```bash
git checkout -b feature/nouvelle-fonctionnalite
```

2. Développer dans le notebook
3. Mettre à jour les requirements si nécessaire :

```bash
pip freeze > requirements-full.txt
```

4. Commiter et pousser :

```bash
git add .
git commit -m "Ajout de nouvelle fonctionnalité"
git push origin feature/nouvelle-fonctionnalite
```

### Tests et Validation

- Exécuter toutes les cellules du notebook
- Vérifier les données en base
- Valider les visualisations

## 🐛 Résolution de Problèmes

### Erreur de Connexion MySQL

```bash
# Vérifier que MySQL est démarré
sudo systemctl status mysql

# Vérifier les credentials dans .env
cat .env
```

### Problèmes de Dépendances

```bash
# Réinstaller l'environnement
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Erreurs de Données

- Vérifier le format du fichier CSV
- Contrôler les types de données
- Examiner les valeurs manquantes

## 📞 Support

Pour toute question ou problème :

1. Consulter la documentation dans le notebook
2. Vérifier les logs d'erreur
3. Ouvrir une issue sur GitHub
4. Contacter : [MarcTsobgny2321](https://github.com/MarcTsobgny2321)

## 📄 Licence

Ce projet est développé dans le cadre du cours MTI à l'UQAM.

## 🤝 Contribution

Les contributions sont les bienvenues ! Merci de :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

---

**Développé avec ❤️ pour l'économie circulaire**
