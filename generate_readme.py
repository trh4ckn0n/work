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

# Vérifier la réponse
if response.status_code == 200:
    repos = response.json()
elif response.status_code == 401:
    raise Exception("⚠️ Erreur d'authentification : Vérifie ton token GitHub.")
else:
    raise Exception(f"❌ Erreur API GitHub: {response.status_code}")

# Générer un README stylé
readme_content = f"""  
<h1 align="center">🚀 Bienvenue sur mon GitHub !</h1>
<p align="center">
    <img src="https://github.com/trh4ckn0n.png" width="120" alt="Avatar">
</p>

<p align="center">
    🔥 Passionné par la cybersécurité et le développement  
    🌟 Toujours en train d'expérimenter de nouveaux outils  
    🚀 Voici un aperçu de mes projets GitHub !  
</p>

---

### 📂 Mes Repositories
| 🔹 Nom | 📝 Description | 💻 Langage | ⭐ Stars | 🍴 Forks | 🕒 Dernière MAJ |
|--------|--------------|------------|---------|---------|---------------|
"""

# Ajouter les repositories sous forme de tableau
for repo in repos:
    name = repo['name']
    description = repo['description'] or "Aucune description"
    language = repo['language'] or "Non spécifié"
    stars = repo['stargazers_count']
    forks = repo['forks_count']
    updated_at = datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b %Y')

    readme_content += f"| [{name}](https://github.com/{GITHUB_USERNAME}/{name}) | {description} | {language} | {stars}⭐ | {forks}🍴 | {updated_at} |\n"

# Ajouter une section de contact
readme_content += """
---

### 📬 Me Contacter :
- 💻 [Mon GitHub](https://github.com/trh4ckn0n)
- ✈️ Telegram : [@trh4ckn0n](https://t.me/trh4ckn0n)
- 📧 Email : *trhacknon@proton.me*

---

🚀 *Merci d'avoir visité mon GitHub !* 🎉  
"""

# Écrire dans le README.md
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(readme_content)

print("✅ README mis à jour avec succès !")
