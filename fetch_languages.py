import os
import requests
import matplotlib.pyplot as plt

# Sicherstellen, dass matplotlib keinen Display benötigt
import matplotlib
matplotlib.use('Agg')

# Token und Header für die GitHub API
token = os.getenv('STATS_TOKEN')
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

# Liste Ihrer Repositories
repos = ['navpav2002/react-int', 'navpav2002/Assembly', 'navpav2002/Docker_INT', 'navpav2002/JS-AA1']

# Sammeln der Sprachdaten
all_languages = {}

for repo in repos:
    response = requests.get(f'https://api.github.com/repos/{repo}/languages', headers=headers)
    if response.ok:
        repo_languages = response.json()
        for language, size in repo_languages.items():
            all_languages[language] = all_languages.get(language, 0) + size
    else:
        print(f"Fehler beim Abrufen der Daten für Repo {repo}")

# Erstellen des Balkendiagramms
languages = list(all_languages.keys())
sizes = list(all_languages.values())

# Dunklen Hintergrund für das Diagramm einstellen
plt.figure(figsize=(10, 8))
plt.bar(languages, sizes, color='blue')
plt.title('Programming Languages Usage')
plt.xlabel('Languages')
plt.ylabel('Bytes of Code')
plt.style.use('dark_background')

# Speichern des Diagramms als Bild
diagram_path = 'languages_usage_chart.png'
plt.savefig(diagram_path, facecolor='black')

# Sicherstellen, dass das Bild korrekt gespeichert wurde
if os.path.exists(diagram_path):
    print(f"Balkendiagramm wurde als {diagram_path} gespeichert.")
else:
    print("Fehler beim Speichern des Balkendiagramms.")

