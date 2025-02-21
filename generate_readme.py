import os
import requests
from datetime import datetime

# Obtenir le token GitHub depuis les variables d'environnement
GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")
GITHUB_USERNAME = "trh4ckn0n"

# URL de l'API pour récupérer tous les repos de l'utilisateur
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

# Headers pour l'authentification
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Effectuer la requête pour récupérer les repositories
response = requests.get(GITHUB_API_URL, headers=headers)
if response.status_code == 200:
    repos = response.json()
elif response.status_code == 401:
    raise Exception("⚠️ Erreur d'authentification : Vérifie ton token GitHub.")
else:
    raise Exception(f"❌ Erreur API GitHub: {response.status_code}")

# Générer un README stylé
readme_content = """
<h1 align="center" style="color: #39FF14; text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;">😈 Bienvenue sur mon GitHub !</h1>

<p align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=30&duration=3200&color=FF5733&background=000000&center=true&vCenter=true&width=550&height=70&lines=Hi+Im+TRHACKNON" 
    style="border: 3px solid #FF0000; box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;" />
</p>
<p align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=30&duration=3200&color=39FF14&background=000000&center=true&vCenter=true&width=550&height=70&lines=Welcome+to+my+GitHub!+👋" 
    style="border: 3px solid #FF0000; box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;" />
</p>
<p align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=30&duration=3200&color=00FFFF&background=000000&center=true&vCenter=true&width=550&height=70&lines=Cybersecurity+%26+Development" 
    style="border: 3px solid #FF0000; box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;" />
</p>
<p align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=30&duration=6400&color=FF00FF&background=000000&center=true&vCenter=true&width=550&height=70&lines=Pentester+|+Coder+|+Hacktivist" 
    style="border: 3px solid #FF0000; box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;" />
</p>

<p align="center">
    <img src="https://github.com/trh4ckn0n.png" width="120" alt="Avatar" style="border-radius: 50%; border: 3px solid #39FF14; box-shadow: 0 0 15px #39FF14;"/>
</p>

<p align="center">
    <img width="150" src="https://komarev.com/ghpvc/?username=trh4ckn0n&label=Profile%20Visitor&color=071A2C&style=for-the-badge" alt="Profile Visitors Badge" style="border: 2px solid #39FF14;"/>
</p>

<p align="center">
    <img width="280" align="center" src="https://github-widgetbox.vercel.app/api/profile?username=trh4ckn0n&data=followers,repositories,stars,commits&theme=radical&background=0D1117&border_radius=10&padding=15" style="border: 3px solid #FF0000; box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;" />
</p>

<p align="center" style="color: #39FF14; font-size: 1.2em; text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;">
    👾 Passionné par la cybersécurité et le développement  
    🌟 Toujours en train d'expérimenter de nouveaux outils  
    🚀 Voici un aperçu de mes projets GitHub !  
</p>

<p align="center"><img src="https://raw.githubusercontent.com/khoa083/khoa/main/Khoa_ne/img/Rainbow.gif" width="100%" style="border-radius: 5px; border: 3px solid #39FF14; box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;" /></p>

### 📂 Mes Repositories
| 🔹 Nom | 📝 Description | 💻 Langage | ⭐ Stars | 🍴 Forks | 🕒 Dernière MAJ | 🌍 GitHub Pages |
|--------|--------------|------------|---------|---------|---------------|-----------------|
"""

for repo in repos:
    name = repo['name']
    description = repo['description'] or "Aucune description"
    language = repo['language'] or "Non spécifié"
    stars = repo['stargazers_count']
    forks = repo['forks_count']
    updated_at = datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b %Y')

    # Vérifier si GitHub Pages est activé
    pages_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{name}/pages"
    pages_response = requests.get(pages_url, headers=headers)
    github_pages = f"[🌍 Voir ici](https://{GITHUB_USERNAME}.github.io/{name}/)" if pages_response.status_code == 200 else "❌"

    # Ajout du retour à la ligne pour bien séparer les repos
    readme_content += f"| [{name}](https://github.com/{GITHUB_USERNAME}/{name}) | {description} | {language} | {stars}⭐ | {forks}🍴 | {updated_at} | {github_pages} |\n"
# Écrire dans le README.md
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(readme_content)

print("✅ README mis à jour avec succès !")
