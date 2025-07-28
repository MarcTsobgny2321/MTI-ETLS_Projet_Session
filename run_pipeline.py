# Exemple d'orchestration du pipeline ETL avec nbconvert
import subprocess
import os
import sys
import pandas as pd
import shutil
from math import ceil
import time
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer
import psutil

folders_to_remove = ['dataset', 'generated', 'out_process']
# Supprimer les dossiers listés dans folders_to_remove s'ils existent
if '--refresh' in sys.argv:
    for folder in folders_to_remove:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Dossier supprimé : {folder}")

notebooks = [
    'process/01_Extraction.ipynb',
    'process/02_Transformation.ipynb',
    'process/03_Load.ipynb',
    'process/04_Analyse_Exploratoire.ipynb',
    'process/05_Visualisation_Geospatiale.ipynb',
    'process/06_BI_Build_Element_Tableaux_de_Bord.ipynb',
    'process/07_BI_Generate_Dashboard_template.ipynb'
    # Ajoutez d'autres notebooks si besoin
]

# Exécuter le pipeline seulement si '--start' n'est pas dans les arguments
if '--start' not in sys.argv:
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



print("Démarrer automatiquement un serveur HTTP pour le dashboard et ouvrir la page dans le navigateur \n")

# Charger le port depuis .env si disponible, sinon utiliser 5050
def get_port(default=5050):
    port = default
    env_path = os.path.abspath('.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.strip().startswith('PORT='):
                    try:
                        port = int(line.strip().split('=', 1)[1])
                    except Exception:
                        pass
    return port

def stop_all_python_on_port(port):
    print(f"🔎 Recherche de tous les processus Python utilisant le port {port}...")
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] and 'python' in proc.info['name'].lower():
                for conn in proc.net_connections(kind='inet'):
                    if conn.laddr.port == port:
                        print(f"🛑 Arrêt du processus Python PID {proc.info['pid']} sur le port {port}")
                        proc.terminate()
        except Exception:
            pass

print("🔄 Lecture du port HTTP dans le fichier .env (défaut : 5050)...")
port = get_port(5050)
print(f"➡️  Port choisi pour le serveur HTTP : {port}")

stop_all_python_on_port(port)
print("✅ Tous les serveurs Python utilisant ce port ont été arrêtés (si présents).")

dashboard_dir = os.path.abspath('generated')
dashboard_file = 'dashboard.html'
print(f"📂 Dossier du dashboard : {dashboard_dir}")
print(f"📄 Fichier dashboard : {dashboard_file}")

def start_server():
    print(f"🚀 Démarrage du serveur HTTP sur le port {port}...")
    os.chdir(dashboard_dir)
    handler = SimpleHTTPRequestHandler
    httpd = HTTPServer(('localhost', port), handler)
    print(f"✅ Serveur HTTP lancé sur http://localhost:{port}/")
    print("🌐 Ouverture du dashboard dans le navigateur...")
    webbrowser.open(f'http://localhost:{port}/{dashboard_file}')
    print(f"🌐 Dashboard ouvert dans le navigateur : http://localhost:{port}/{dashboard_file}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("🛑 Arrêt manuel du serveur HTTP (Ctrl+C détecté).")
        httpd.server_close()

# Lancer le serveur dans le thread principal pour garder le terminal ouvert
print("⏳ Démarrage du serveur HTTP dans le terminal principal (Ctrl+C pour arrêter)...")
start_server()
