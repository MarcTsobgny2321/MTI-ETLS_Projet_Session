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

## Structure principale

```
MTI/
├── process/                # Notebooks ETL, analyse, dashboard
├── dataset/                  # Données sources et résultats intermédiaires
├── .env                      # Variables d’environnement (à créer)
├── requirements.txt          # Dépendances
└── README.md                 # Ce guide
```

## Support

Pour toute question, ouvrez une issue sur GitHub ou contactez [MarcTsobgny2321](https://github.com/MarcTsobgny2321).

---

**Développé pour l’économie circulaire – MTI UQAM**
