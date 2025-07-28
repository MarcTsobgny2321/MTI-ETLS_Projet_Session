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

4. **Configurer le l'environnement**

   - Renseigner vos paramètres dans le fichier `.env` en vous referent au ficher `.env.example`

5. **Lancer Jupyter Notebook ou votre editer de choix**

   ```bash
   jupyter notebook
   ```

   ```bash
   code .
   ```

6. **Exécuter le pipeline ETL et les notebooks d’analyse**
   - Suivez l’ordre des notebooks pour extraire, transformer, analyser et visualiser vos données.

## Exécution automatique du projet

Pour automatiser l'ensemble du pipeline ETL, l'analyse et la génération du dashboard, exécutez simplement le script suivant :

```bash
python run_pipeline.py --refresh
```

Start only http server

```bash
python run_pipeline.py --start
```

Ce script orchestre l'exécution des notebooks dans le bon ordre, gère les dépendances et génère automatiquement le dashboard HTML final dans le dossier `generated/`. Le dashboard s'ouvre ensuite dans votre navigateur par défaut.

---

## Structure principale

```
MTI/
├── process/                        # Notebooks ETL, analyse, visualisation, dashboard, documentation
│   ├── 00_Assemblage.ipynb         # Acquisition et structuration des données
│   ├── 01_ETL_FaitsMatieres.ipynb  # Extraction et transformation des faits matières
│   ├── 02_ETL_Dimensions.ipynb     # Construction des dimensions (producteur, site, matière, temps)
│   ├── 03_Load.ipynb               # Chargement et persistance des données structurées
│   ├── 04_Visualisation_Geospatiale.ipynb # Cartographie et analyses spatiales
│   ├── 05_Visualisation_Geospatiale.ipynb # Visualisation géospatiale avancée
│   ├── 06_BI_Build_Element_Tableaux_de_Bord.ipynb # Indicateurs, KPIs, tableaux de bord
│   └── 99_Documentation.ipynb      # Rapport synthétique et business
├── dataset/                        # Données sources et résultats intermédiaires (CSV, JSON)
├── generated/                      # Outputs : dashboard HTML, graphiques, cartes, CSV normalisés
│   ├── dashboard.html              # Dashboard interactif généré automatiquement
│   ├── graphs/                     # Graphiques PNG
│   ├── normalized/                 # Données normalisées
│   └── sites/                      # Cartes interactives HTML
├── out_process/                    # Notebooks/outils intermédiaires ou archivés
├── cache/                          # Fichiers de cache (ex : géocodage)
├── ref/                            # Référentiels, documentation, sources externes (PDF, etc.)
├── .env                            # Variables d’environnement (à créer)
├── .env.example                    # Exemple de configuration d’environnement
├── requirements.txt                # Dépendances Python
├── run_pipeline.py                 # Script d’orchestration du pipeline complet
├── README.md                       # Ce guide
└── POC_Presentation.md             # Présentation métier et technique du POC
```

## Support

**Développé pour l’économie circulaire – MTI UQAM & ETS**

```

```
