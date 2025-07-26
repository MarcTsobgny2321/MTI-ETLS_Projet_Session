git commit -m "Ajout de nouvelle fonctionnalité"
git push origin feature/nouvelle-fonctionnalite

# Projet BI – Économie Circulaire

## Setup rapide

1. **Cloner le projet**

   ```bash
   git clone https://github.com/MarcTsobgny2321/MTI-ETLS_Projet_Session.git
   cd MTI-ETLS_Projet_Session
   ```

2. **Créer et activer l’environnement virtuel**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données**

   - Renseigner vos paramètres dans le fichier `.env` (voir exemple dans le projet)

5. **Lancer Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

6. **Exécuter le pipeline ETL et les notebooks d’analyse**
   - Suivez l’ordre des notebooks pour extraire, transformer, analyser et visualiser vos données.

## Exécution automatique du projet

Pour automatiser l'ensemble du pipeline ETL, l'analyse et la génération du dashboard, exécutez simplement le script suivant :

```bash
python run_pipeline.py
```

Ce script orchestre l'exécution des notebooks dans le bon ordre, gère les dépendances et génère automatiquement le dashboard HTML final dans le dossier `generated/`. Le dashboard s'ouvre ensuite dans votre navigateur par défaut.

---

## Structure principale

MTI/
├── process/ # Notebooks ETL, analyse, dashboard
│ ├── 00_Assemblage.ipynb # Acquisition et structuration des données
│ ├── 04_Visualisation_Geospatiale.ipynb # Cartographie et analyses spatiales
│ ├── 05_Tableaux_de_Bord.ipynb # Indicateurs et visualisations
│ ├── 06_BI_Build_Dashboard.ipynb # Génération du dashboard HTML
│ └── 99_Documentation.ipynb # Rapport synthétique et business
├── dataset/ # Données sources et résultats intermédiaires
├── generated/ # Outputs : dashboard HTML, graphiques, cartes
│ ├── dashboard.html # Dashboard interactif généré automatiquement
│ ├── graphs/ # Graphiques PNG
│ └── sites/ # Cartes interactives HTML
├── .env # Variables d’environnement (à créer)
├── requirements.txt # Dépendances
└── README.md # Ce guide

```

## Support

**Développé pour l’économie circulaire – MTI UQAM & ETS**
```
