# Exemple d'orchestration du pipeline ETL avec nbconvert
import subprocess
import os
import sys
import time
import pandas as pd

notebooks = [
    'process/00_Assemblage.ipynb',
    'process/01_ETL_FaitsMatieres.ipynb',
    'process/02_ETL_Dimensions.ipynb',
    'process/03_Analyse_Exploratoire.ipynb',
    'process/04_Visualisation_Geospatiale.ipynb',
    'process/05_Tableaux_de_Bord.ipynb'
    # Ajoutez d'autres notebooks si besoin
]

output_folder = 'out_process'
if not os.path.exists(output_folder):
    os.makedirs(output_folder, exist_ok=True)

for nb in notebooks:
    print(f"Exécution de {nb}...")
    cmd = [
        "jupyter", "nbconvert", "--to", "notebook", "--execute",
        "--output", os.path.basename(nb),
        "--output-dir", output_folder,
        nb
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Erreur lors de l'exécution de {nb} : {result.stderr}")
        print("Arrêt du pipeline.")
        sys.exit(result.returncode)

file_path = '../dataset/faits_matieres.csv'  # Adaptez le chemin si besoin
timeout = 30  # secondes
waited = 0
while not os.path.exists(file_path) and waited < timeout:
    print(f"Attente de la création du fichier {file_path}...")
    time.sleep(2)
    waited += 2
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Le fichier {file_path} n'a pas été trouvé après {timeout} secondes.")

faits_matieres = pd.read_csv(file_path)

print("Pipeline ETL/BI terminé.")