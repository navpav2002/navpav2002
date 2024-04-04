import os
import requests

# Замените 'owner/repo' на владельца и название вашего репозитория
repo = 'owner/repo'
token = os.getenv('STATS_TOKEN')

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get(f'https://api.github.com/repos/{repo}/languages', headers=headers)
languages = response.json()

# Преобразование статистики языков в строку для сохранения в файл
languages_str = '\n'.join([f'{lang}: {size}' for lang, size in languages.items()])

# Сохранение статистики языков в файл
with open('LANGUAGES.md', 'w') as file:
    file.write(languages_str)
