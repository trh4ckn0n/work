import os
import requests
from datetime import datetime

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
readme_content = "# 🚀 Mes Repositories GitHub\n\n"
readme_content += "Voici une liste de mes repositories GitHub avec des détails supplémentaires, présentée de manière fun et interactive ! 🎉\n\n"

# Ajouter des badges au début du README
readme_content += """
[![Maj le README avec les repositories GitHub](https://github.com/trh4ckn0n/work/actions/workflows/update_readme.yml/badge.svg?event=workflow_run)](https://github.com/trh4ckn0n/work/actions/workflows/update_readme.yml)
![Last Commit](https://img.shields.io/github/last-commit/trh4ckn0n/work?style=flat-square)
![Stars](https://img.shields.io/github/stars/trh4ckn0n/work?style=flat-square)
![Forks](https://img.shields.io/github/forks/trh4ckn0n/work?style=flat-square)
\n\n"""

# Parcourir les repos et ajouter leurs détails
for repo in repos:
    name = repo['name']
    description = repo['description'] or "Pas de description disponible"
    language = repo['language'] or "Non spécifié"
    stars = repo['stargazers_count']
    forks = repo['forks_count']
    updated_at = datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %B %Y')

    # Ajouter les informations du repo au README avec un lien cliquable
    readme_content += f"### [{name}](https://github.com/trh4ckn0n/{name})\n"
    readme_content += f"- **Description**: {description}\n"
    readme_content += f"- **Langage principal**: {language}\n"
    readme_content += f"- **Étoiles**: {stars} 🌟\n"
    readme_content += f"- **Forks**: {forks} 🍴\n"
    readme_content += f"- **Dernière mise à jour**: {updated_at} 🕒\n\n"

# Ajouter des liens supplémentaires vers des outils utiles
readme_content += """
## 🚀 Liens Utiles :
- [Documentation API GitHub](https://docs.github.com/en/rest) 📚
- [Mon Profil GitHub](https://github.com/trh4ckn0n) 👨‍💻
- [Suivre mes autres projets](https://github.com/trh4ckn0n?tab=repositories) 📂
\n\n"""

# Ajouter un message de clôture
readme_content += """
Merci de visiter mon GitHub ! 🎉
"""

# Écrire le contenu dans le README
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("README mis à jour avec succès ! 🎉")
