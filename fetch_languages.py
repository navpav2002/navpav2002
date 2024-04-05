import os
import requests
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')

plt.style.use('dark_background')

token = os.getenv('STATS_TOKEN')
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

repos = [
    'navpav2002/react-int',
    'navpav2002/Assembly',
    'navpav2002/Docker_INT',
    'navpav2002/JS-AA1'
]

all_languages = {}

for repo in repos:
    response = requests.get(f'https://api.github.com/repos/{repo}/languages', headers=headers)
    if response.ok:
        repo_languages = response.json()
        for language, size in repo_languages.items():
            all_languages[language] = all_languages.get(language, 0) + size
    else:
        print(f"Fehler beim Abrufen der Daten für Repo {repo}: {response.text}")

colors = ['#33FFF3', '#008000', '#0000ff', '#ffff00', '#FF33F0', '#ff0000']

languages = list(all_languages.keys())
sizes = list(all_languages.values())

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.bar(languages, sizes, color=colors)

ax.set_facecolor('black')

ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.xlabel('Languages', color='white')
plt.ylabel('Bytes of Code', color='white')
plt.title('Programming Languages Usage', color='white')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, f'{int(yval)}', va='bottom', ha='center', color='white')

for spine in ax.spines.values():
    spine.set_color('white')
    
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(which='major', linestyle='--', linewidth=0.5, color='grey')  
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='grey') 

diagram_path = 'languages_usage_chart.png'
plt.savefig(diagram_path, bbox_inches='tight', facecolor='black')

if os.path.exists(diagram_path):
    print(f"Balkendiagramm wurde als {diagram_path} gespeichert.")
else:
    print("Fehler beim Speichern des Balkendiagramms.")
