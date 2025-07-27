# Présentation du POC – Projet BI Économie Circulaire

## Contexte et objectifs

Ce POC (Proof of Concept) vise à démontrer la faisabilité et la valeur ajoutée d’une solution BI pour l’économie circulaire, en automatisant la collecte, le traitement et la visualisation des données sur les matières résiduelles et leur valorisation.

- Centraliser et fiabiliser les données issues de sources variées (CSV, Excel, GeoJSON)
- Fournir des indicateurs clés pour le pilotage et l’optimisation des flux
- Faciliter la communication et la transparence auprès des parties prenantes

## Architecture et workflow

- **Pipeline ETL automatisé** : Extraction, transformation et chargement des données via des notebooks Jupyter modulaires
- **Orchestration** : Script Python (`run_pipeline.py`) pour exécuter l’ensemble du workflow et générer les outputs
- **Dashboard HTML interactif** : Généré automatiquement à la fin du pipeline, accessible sur le réseau local via un serveur HTTP intégré
- **Documentation métier** : Rapport synthétique pour les parties prenantes non techniques

## Fonctionnalités clés

- Téléchargement et conversion automatique des données sources
- Nettoyage, structuration et modélisation métier
- Visualisations avancées : graphiques, KPIs, cartographies interactives
- Dashboard HTML avec titres descriptifs, accessible sur [http://localhost:5050/dashboard.html](http://localhost:5050/dashboard.html)
- Serveur HTTP interne pour le partage instantané et sécurisé sur le réseau local

### Exemple de capture d’écran du dashboard

> _À insérer ici : Capture d’écran du dashboard interactif généré_

---

## Avantages du serveur HTTP interne

## Comparatif avec les solutions cloud (Azure, AWS, GCP...)

- **Simplicité et rapidité de mise en œuvre** : Pas de configuration complexe ni de coûts liés à l’infrastructure cloud
- **Maîtrise des données** : Les données sensibles restent sur le réseau local, sans exposition externe
- **Coût réduit** : Pas de frais d’hébergement, de stockage ou de licences cloud
- **Indépendance technologique** : Solution open-source, facilement adaptable et sans dépendance à un fournisseur
- **Flexibilité** : Possibilité d’évolution vers le cloud ou d’intégration avec des services externes si besoin

---

## Structure du projet

```
MTI/
├── process/                  # Notebooks ETL, analyse, dashboard
│   ├── 00_Assemblage.ipynb   # Acquisition et structuration des données
│   ├── 04_Visualisation_Geospatiale.ipynb # Cartographie et analyses spatiales
│   ├── 05_Tableaux_de_Bord.ipynb          # Indicateurs et visualisations
│   ├── 06_BI_Build_Dashboard.ipynb        # Génération du dashboard HTML
│   └── 99_Documentation.ipynb             # Rapport synthétique et business
├── dataset/                  # Données sources et résultats intermédiaires
├── generated/                # Outputs : dashboard HTML, graphiques, cartes
│   ├── dashboard.html        # Dashboard interactif généré automatiquement
│   ├── graphs/               # Graphiques PNG
│   └── sites/                # Cartes interactives HTML
├── .env                      # Variables d’environnement (à créer)
├── requirements.txt          # Dépendances
└── README.md                 # Ce guide
```

## Démonstration

1. Préparer l’environnement et installer les dépendances
2. Exécuter le script `run_pipeline.py` pour lancer le pipeline complet
3. Le dashboard s’ouvre automatiquement dans le navigateur et est accessible sur le réseau local
4. Utiliser le rapport métier pour présenter les apports business

### Capture d’écran : Ouverture du dashboard dans le navigateur

> _À insérer ici : Capture d’écran de l’accès au dashboard via le serveur HTTP_

---

## Conclusion

Ce POC montre la capacité à automatiser et valoriser les données de l’économie circulaire, avec un dashboard interactif et partageable, et une documentation adaptée aux besoins des décideurs et parties prenantes.

## Migration vers une solution cloud

Ce POC peut facilement évoluer vers une solution ETL et BI Cloud (Azure Data Factory, AWS Glue, Google Dataflow, Power BI, Tableau, etc.) :

- Conteneurisation des notebooks et scripts (Docker)
- Déploiement sur des services cloud (VM, Kubernetes, App Services)
- Stockage des données sur des bases cloud (Blob Storage, S3, SQL)
- Automatisation et orchestration via des plateformes ETL cloud (Azure Data Factory, AWS Glue, Google Dataflow)
- Visualisation et reporting avancés avec des outils BI cloud (Power BI, Tableau, Google Data Studio)
- Sécurisation et gestion des accès via les outils natifs du cloud
- Monitoring, scalabilité et haute disponibilité pour une utilisation en production

### Étapes de migration vers une solution ETL et BI Cloud

1. **Analyse et préparation du code**

   - Identifier les notebooks et scripts clés (ETL, visualisation, dashboard)
   - Séparer la logique métier, le traitement des données et la génération des outputs
   - Documenter les dépendances (requirements.txt, .env)

2. **Conteneurisation**

   - Créer un Dockerfile pour encapsuler l’environnement Python et les notebooks
   - Tester l’exécution du pipeline dans un conteneur local

3. **Stockage des données dans le cloud**

   - Migrer les fichiers sources (CSV, Excel, GeoJSON) vers un stockage cloud (Azure Blob, AWS S3, Google Cloud Storage)
   - Adapter les scripts pour lire/écrire directement depuis/vers le cloud

4. **Orchestration ETL dans le cloud**

   - Déployer les notebooks/scripts sur une plateforme ETL cloud (Azure Data Factory, AWS Glue, Google Dataflow)
   - Configurer les pipelines pour automatiser l’extraction, la transformation et le chargement

5. **Génération et hébergement du dashboard BI**

   - Adapter la génération du dashboard HTML pour l’hébergement sur un service web cloud (App Service, S3 static website, etc.)
   - Intégrer les visualisations dans un outil BI cloud (Power BI, Tableau, Google Data Studio) si besoin

6. **Sécurisation et gestion des accès**

   - Mettre en place l’authentification et la gestion des droits d’accès via les outils natifs du cloud

7. **Monitoring, scalabilité et maintenance**

   - Activer le monitoring et les alertes sur les pipelines et les dashboards
   - Prévoir la scalabilité pour gérer des volumes de données croissants

8. **Documentation et formation**
   - Mettre à jour la documentation métier et technique pour l’environnement cloud
   - Former les utilisateurs et administrateurs à la nouvelle solution

---

---

---

## Annexes techniques

### Extrait de code : Orchestration du pipeline

> _À insérer ici : Portion de code du script `run_pipeline.py` ou d’un notebook clé_

### Extrait de code : Génération du dashboard HTML

> _À insérer ici : Portion de code illustrant la génération du dashboard_

---

**Développé pour l’économie circulaire – MTI UQAM & ETS**
