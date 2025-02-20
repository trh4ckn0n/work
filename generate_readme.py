import os
import requests

# Obtenir le token d'authentification depuis les secrets GitHub
GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")

# L'API GitHub pour obtenir les repositories
GITHUB_API_URL = "https://api.github.com/users/trh4ckn0n/repos"

# Headers avec le token d'authentification
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Faire la requête pour obtenir les repos
response = requests.get(GITHUB_API_URL, headers=headers)

# Vérifier si la réponse est correcte
if response.status_code == 200:
    repos = response.json()
else:
    raise Exception(f"Erreur de l'API GitHub: {response.status_code}")

# Créer le contenu du README avec des informations détaillées
readme_content = "# Mes Repositories GitHub\n\nVoici une liste de mes repositories GitHub avec des détails supplémentaires :\n\n"

for repo in repos:
    name = repo['name']
    description = repo['description'] or "Pas de description disponible"
    language = repo['language'] or "Non spécifié"
    stars = repo['stargazers_count']
    forks = repo['forks_count']
    updated_at = repo['updated_at']

    readme_content += f"### {name}\n"
    readme_content += f"- **Description**: {description}\n"
    readme_content += f"- **Langage principal**: {language}\n"
    readme_content += f"- **Étoiles**: {stars}\n"
    readme_content += f"- **Forks**: {forks}\n"
    readme_content += f"- **Dernière mise à jour**: {updated_at}\n\n"

# Écrire le contenu dans le README
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
