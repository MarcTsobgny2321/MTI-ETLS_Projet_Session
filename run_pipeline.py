# Exemple d'orchestration du pipeline ETL avec nbconvert
import subprocess
import os
import sys
import time
import pandas as pd
import shutil
from math import ceil

folders_to_remove = ['dataset', 'generated', 'out_process']
# Supprimer les dossiers listés dans folders_to_remove s'ils existent
for folder in folders_to_remove:
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"Dossier supprimé : {folder}")

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

total_nb = len(notebooks)
for idx, nb in enumerate(notebooks, 1):
    progress = ceil((idx / total_nb) * 50)  # 50 caractères pour la barre
    bar = '[' + '#' * progress + '-' * (50 - progress) + f'] {idx}/{total_nb}'
    print(f"Progression : {bar}")
    print(f"Exécution de {nb}...")
    cmd = [
        "jupyter", "nbconvert", "--to", "notebook", "--execute",
        "--output", os.path.basename(nb),
        "--output-dir", output_folder,
        nb
    ]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    nb_prefix = f"[{os.path.basename(nb)}] "
    while True:
        output = process.stdout.readline()
        if output:
            print(nb_prefix + output.strip())
        err = process.stderr.readline()
        if err:
            print(nb_prefix + "[stderr] " + err.strip())
        if output == '' and err == '' and process.poll() is not None:
            break
    returncode = process.poll()
    if returncode != 0:
        print(f"Erreur lors de l'exécution de {nb}")
        print("Arrêt du pipeline.")
        sys.exit(returncode)


print("🎉 Pipeline ETL/BI terminé avec succès ! 🎉")
print(r"""
    ______________________
       |                      |
       |   DATA WAREHOUSE     |
       |______________________|
     /   /   /   /   /   /
    /___/___/___/___/___/
       | BI DASHBOARDS      |
       |   📊 📈 📉         |
       |____________________|
    \  🚀  🎉  🤖  /
     `--------------`
Bravo ! Vos données sont prêtes pour l'analyse BI ! 🚀✨
""")
