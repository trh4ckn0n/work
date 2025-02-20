import os
import requests
from datetime import datetime

# Obtenir le token d'authentification depuis les secrets GitHub
GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")
GITHUB_USERNAME = "trh4ckn0n"

# API GitHub pour obtenir les repositories
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

# Headers avec le token d'authentification
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Faire la requête pour obtenir les repos
response = requests.get(GITHUB_API_URL, headers=headers)

# Vérifier si la réponse est correcte
if response.status_code != 200:
    print(f"Erreur: {response.status_code} - {response.json().get('message', 'Erreur inconnue')}")
    exit(1)

repos = sorted(response.json(), key=lambda r: r['updated_at'], reverse=True)

# Créer le contenu du README
readme_content = f"""
# 🚀 Bienvenue sur mon GitHub, je suis {GITHUB_USERNAME} !

```python
   _____ _          _    _                
  |_   _| |_  __ _ | |_ (_)__ _ _ _ _  _  
    | | | ' \/ _` ||  _|| / _` | '_| || |
    |_| |_||_\__,_| \__||_\__,_|_|  \_, |
                                    |__/ 
```

Je suis passionné par le développement, la cybersécurité et le hacking éthique. Découvrez mes projets et explorations techniques ci-dessous !

---
## 📊 Mes Statistiques GitHub

![Profil Views](https://komarev.com/ghpvc/?username={GITHUB_USERNAME}&color=blue)
![Followers](https://img.shields.io/github/followers/{GITHUB_USERNAME}?style=social)
![Stars](https://img.shields.io/github/stars/{GITHUB_USERNAME}?style=social)

---
## 📂 Mes Repositories

| Nom | Description | Langage | ⭐ Stars | 🍴 Forks | 🕒 Dernière Maj |
|------|------------|---------|---------|---------|----------------|
"""

# Ajouter les repos dans un tableau stylé
for repo in repos:
    name = repo['name']
    description = repo['description'] or "Aucune description"
    language = repo['language'] or "Non spécifié"
    stars = repo['stargazers_count']
    forks = repo['forks_count']
    updated_at = datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %B %Y')
    readme_content += f"| [{name}](https://github.com/{GITHUB_USERNAME}/{name}) | {description} | {language} | {stars} ⭐ | {forks} 🍴 | {updated_at} |"

readme_content += """

---
## 📫 Contact

📌 [Mon GitHub](https://github.com/{GITHUB_USERNAME})  
📌 [Telegram](https://t.me/{GITHUB_USERNAME})  

Merci d'avoir visité mon GitHub ! 🎉

---
*Dernière mise à jour : {datetime.utcnow().strftime('%d %B %Y à %H:%M UTC')}*
"""

# Écrire dans le fichier README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("README mis à jour avec succès ! 🚀")
