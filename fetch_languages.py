import os
import requests
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')

# Token und Header für die GitHub API
token = os.getenv('STATS_TOKEN')
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

repos = ['navpav2002/react-int', 'navpav2002/Assembly', 'navpav2002/Docker_INT', 'navpav2002/JS-AA1']

all_languages = {}

for repo in repos:
    response = requests.get(f'https://api.github.com/repos/{repo}/languages', headers=headers)
    if response.ok:
        repo_languages = response.json()
        for language, size in repo_languages.items():
            all_languages[language] = all_languages.get(language, 0) + size
    else:
        print(f"Fehler beim Abrufen der Daten für Repo {repo}")

plt.figure(figsize=(10, 8))
plt.bar(all_languages.keys(), all_languages.values(), color='blue')
plt.title('Programming Languages Usage')
plt.xlabel('Languages')
plt.ylabel('Bytes of Code')
plt.style.use('dark_background')
plt.savefig('languages_usage_chart.png', facecolor='black')

print(response.json())
print(f'Schreibe Sprachstatistik in LANGUAGES.md: \n{languages_str}')
print(f"Speichern der Daten in {os.path.abspath('LANGUAGES.md')}")
