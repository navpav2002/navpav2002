import os
import requests

token = os.getenv('STATS_TOKEN')
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

# Ersetzen Sie dies mit einer Liste Ihrer Repositories
repos = ['navpav2002/react-int', 'navpav2002/Assembly', 'navpav2002/Docker_INT', 'navpav2002/JS-AA1']

all_languages = {}

for repo in repos:
    response = requests.get(f'https://api.github.com/repos/{repo}/languages', headers=headers)
    repo_languages = response.json()
    for language, size in repo_languages.items():
        if language in all_languages:
            all_languages[language] += size
        else:
            all_languages[language] = size

languages_str = '\n'.join([f'{lang}: {size}' for lang, size in all_languages.items()])

with open('LANGUAGES.md', 'w') as file:
    file.write(languages_str)
print(response.json())
