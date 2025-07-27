# Présentation du POC – Projet BI Économie Circulaire

## Résumé Exécutif

### 1.1 Contexte et enjeux de l'économie circulaire au Québec

Le Québec s’engage résolument dans la transition vers une économie circulaire visant à maximiser la valeur des ressources et réduire la production de déchets. Malgré ces ambitions, plusieurs obstacles persistent : fragmentation des données, manque de traçabilité des flux de matériaux, difficulté à identifier les synergies entre producteurs et acteurs du recyclage/réutilisation. Ces défis freinent l’optimisation économique et environnementale et compliquent la mise en place de politiques efficaces.

### 1.2 Problématique et objectifs du projet

Face à la complexité et à l’opacité des données sur les matières résiduelles, ce projet vise à concevoir une preuve de concept (POC) d’une plateforme d’intelligence d’affaires sur le cloud. Celle-ci centralisera, structurera et analysera des données sur les gisements de matériaux, leurs circuits de réutilisation et les besoins en intrants secondaires. Les objectifs sont d’améliorer la visibilité, la traçabilité et l’identification des opportunités, tout en produisant des indicateurs de performance pour mesurer la circularité et guider les décisions stratégiques.

### 1.3 Principales réalisations et résultats de la POC

La POC a permis de :

- Définir et prioriser des cas d’usage concrets avec des parties prenantes
- Modéliser un premier entrepôt de données infonuagique adapté à l’économie circulaire
- Intégrer des données hétérogènes via des pipelines ETL/ELT
- Élaborer des tableaux de bord interactifs pour visualiser les flux de matériaux
- Démontrer la faisabilité technique et les bénéfices potentiels d’une telle plateforme en termes de traçabilité et d’optimisation

### 1.4 Recommandations et prochaines étapes

Il est recommandé d’étendre la solution à un plus large éventail de secteurs et de matériaux, d’enrichir les sources de données et d’impliquer plus d’acteurs publics et privés. Des fonctionnalités avancées (prédictions de flux, blockchain pour renforcer la confiance) pourraient être ajoutées à plus long terme. Un plan de déploiement progressif et une gouvernance claire des données sont à prévoir.

---

## Introduction

### 2.1 Contexte global de l'économie circulaire et son importance au Québec

L’économie circulaire vise la réduction, la réutilisation et la valorisation des ressources pour limiter les impacts environnementaux et économiques des modèles linéaires. Au Québec, cette approche s’aligne avec les orientations gouvernementales en matière de lutte aux changements climatiques et de gestion responsable des matières résiduelles.

### 2.2 Le rôle de l'intelligence d'affaires et de l'infonuagique

Les solutions BI permettent d’extraire de la valeur à partir de données massives, facilitant la prise de décision par des visualisations et analyses pertinentes. Combinées à l’infonuagique, elles offrent scalabilité, flexibilité et puissance de calcul pour traiter des données hétérogènes et volumineuses, tout en assurant leur disponibilité et leur sécurité.

### 2.3 Problématique détaillée de la traçabilité et des flux de matériaux

Actuellement, les données relatives aux sous-produits, résidus et intrants secondaires sont dispersées, non standardisées et difficiles d’accès. Cela entraîne un manque de visibilité globale, empêche d’identifier des synergies et compromet la confiance dans la qualité et la provenance des matières. La mise en place d’une traçabilité fiable est donc un levier stratégique pour stimuler l’économie circulaire.

### 2.4 Objectifs spécifiques du projet de POC

- Centraliser et structurer les données des acteurs concernés
- Offrir des visualisations claires et interactives des flux de matériaux
- Démontrer la faisabilité d’une plateforme infonuagique adaptée
- Tester des indicateurs de performance environnementale et économique
- Valider l’intérêt et l’utilité d’une telle solution auprès des parties prenantes

---

## Analyse des Besoins et Cas d'Usage

### 3.1 Parties prenantes et attentes

- Entreprises générant des sous-produits ou déchets
- Entreprises de recyclage, valorisation et réutilisation
- Instances gouvernementales
- Associations industrielles
- Citoyens et groupes environnementaux

Attentes : transparence, simplicité d’accès aux données, valorisation des opportunités de synergie, conformité réglementaire.

### 3.2 Secteur ou type de matériau ciblé pour la POC

La POC se concentre sur un secteur précis (ex : plastiques agricoles en Montérégie, résidus de construction) pour valider la méthodologie avant un élargissement à d’autres flux de matières.

### 3.3 Cas d'usage spécifiques

- Identification et cartographie des gisements de matériaux secondaires
- Mise en relation entre producteurs de déchets et utilisateurs potentiels
- Optimisation de la logistique de collecte et de traitement
- Suivi de la traçabilité et de la conformité réglementaire

### 3.4 Indicateurs clés de performance (KPIs)

- Taux de valorisation des résidus
- Volume de matières réutilisées
- Réduction des émissions associées
- Économies générées par la symbiose industrielle
- Satisfaction des parties prenantes

---

## Architecture et workflow

- **Pipeline ETL automatisé** : Extraction, transformation et chargement des données via des notebooks Jupyter modulaires
- **Orchestration** : Script Python (`run_pipeline.py`) pour exécuter l’ensemble du workflow et générer les outputs
- **Dashboard HTML interactif** : Généré automatiquement à la fin du pipeline, accessible sur le réseau local via un serveur HTTP intégré
- **Documentation métier** : Rapport synthétique pour les parties prenantes non techniques

---

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

---

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

## Annexes techniques

### Extrait de code : Orchestration du pipeline

> _À insérer ici : Portion de code du script `run_pipeline.py` ou d’un notebook clé_

### Extrait de code : Génération du dashboard HTML

> _À insérer ici : Portion de code illustrant la génération du dashboard_

---

**Développé pour l’économie circulaire – MTI UQAM & ETS**

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
