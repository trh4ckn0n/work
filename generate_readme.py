import requests
import os

# Obtenir le token GitHub depuis les secrets
MY_GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")
GITHUB_USERNAME = "trh4ckn0n"  # Change avec ton pseudo GitHub

# URL de l'API GitHub pour récupérer les repos
url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

headers = {
    "Authorization": f"token {MY_GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("❌ Erreur lors de la récupération des repositories.")
    print(response.json())
    exit(1)

repos = response.json()

# Générer un README.md mis à jour
readme_content = "# 📌 Mes repositories GitHub\n\n"

for repo in repos:
    repo_name = repo["name"]
    repo_url = repo["html_url"]
    readme_content += f"- [{repo_name}]({repo_url})\n"

# Écrire dans README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md mis à jour avec succès.")
