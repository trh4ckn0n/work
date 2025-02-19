import requests
import os

GITHUB_USERNAME = "trh4ckn0n"
TOKEN = os.getenv("MY_GITHUB_TOKEN")

API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

def fetch_repos():
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur API:", response.json())
        return []

def generate_readme(repos):
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(f"# 🚀 Les repositories de {GITHUB_USERNAME}\n\n")
        file.write("## 🌟 Mes meilleurs projets\n\n")
        for repo in sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:5]:
            file.write(f"- [{repo['name']}]({repo['html_url']}) ⭐ {repo['stargazers_count']}\n")
        file.write("\n---\n")
        file.write("## 📂 Tous mes repositories\n\n")
        for repo in repos:
            file.write(f"- [{repo['name']}]({repo['html_url']})\n")

if __name__ == "__main__":
    repos = fetch_repos()
    if repos:
        generate_readme(repos)
