import os
import requests
import matplotlib.pyplot as plt

# Sicherstellen, dass matplotlib keinen Display benötigt
import matplotlib
matplotlib.use('Agg')

# Diagrammstil für dunklen Hintergrund verwenden
plt.style.use('dark_background')

# Token und Header für die GitHub API
token = os.getenv('STATS_TOKEN')
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

# Liste Ihrer Repositories
repos = [
    'navpav2002/react-int',
    'navpav2002/Assembly',
    'navpav2002/Docker_INT',
    'navpav2002/JS-AA1'
]

# Sammeln der Sprachdaten
all_languages = {}

for repo in repos:
    response = requests.get(f'https://api.github.com/repos/{repo}/languages', headers=headers)
    if response.ok:
        repo_languages = response.json()
        for language, size in repo_languages.items():
            all_languages[language] = all_languages.get(language, 0) + size
    else:
        print(f"Fehler beim Abrufen der Daten für Repo {repo}: {response.text}")

# Festlegen einer Liste von Farben für die Balken
colors = ['#33FFF3', '#33FF57', '#3357FF', '#DFFF00', '#FF33F0', '#ff0000']

# Erstellen des Balkendiagramms
languages = list(all_languages.keys())
sizes = list(all_languages.values())

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.bar(languages, sizes, color=colors)

# Hintergrundfarbe der Achsen auf schwarz setzen
ax.set_facecolor('black')

# Beschriftungen und Titel hinzufügen
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.xlabel('Languages', color='white')
plt.ylabel('Bytes of Code', color='white')
plt.title('Programming Languages Usage', color='white')

# Beschriftungen auf den Balken hinzufügen
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, f'{int(yval)}', va='bottom', ha='center', color='white')

# Die weißen Achsenlinien und Ticks sicherstellen
for spine in ax.spines.values():
    spine.set_color('white')
    
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(which='major', linestyle='--', linewidth=0.5, color='grey')  # Hauptachsen
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='grey')  # Nebenachsen

# Speichern des Diagramms als Bild mit einem dunklen Hintergrund
diagram_path = 'languages_usage_chart.png'
plt.savefig(diagram_path, bbox_inches='tight', facecolor='black')

# Sicherstellen, dass das Bild korrekt gespeichert wurde
if os.path.exists(diagram_path):
    print(f"Balkendiagramm wurde als {diagram_path} gespeichert.")
else:
    print("Fehler beim Speichern des Balkendiagramms.")
