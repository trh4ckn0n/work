import requests
import os

# Récupérer le token GitHub depuis les variables d'environnement
token = os.getenv('MY_GITHUB_TOKEN')

# Définir l'en-tête avec l'authentification
headers = {
    'Authorization': f'token {token}'
}

# URL de l'API GitHub pour obtenir les repositories
repos_url = "https://api.github.com/users/<votre-nom-utilisateur>/repos"

# Faire une requête à l'API pour obtenir la liste des repositories
response = requests.get(repos_url, headers=headers)

# Vérifier si la requête a réussi
if response.status_code == 200:
    repos = response.json()
else:
    print("Erreur lors de la récupération des repositories.")
    repos = []

# Ouvrir (ou créer) le fichier README.html pour écrire dedans
with open("README.html", "w") as f:
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<title>Repositories GitHub</title>\n")
    f.write('<style>\n')
    f.write('body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f4; }\n')
    f.write('h1 { text-align: center; color: #333; }\n')
    f.write('table { width: 100%; margin: 20px 0; border-collapse: collapse; }\n')
    f.write('th, td { padding: 12px 15px; text-align: left; border: 1px solid #ddd; }\n')
    f.write('th { background-color: #4CAF50; color: white; }\n')
    f.write('tr:nth-child(even) { background-color: #f9f9f9; }\n')
    f.write('tr:hover { background-color: #ddd; }\n')
    f.write('a { color: #1a73e8; text-decoration: none; }\n')
    f.write('a:hover { text-decoration: underline; }\n')
    f.write('</style>\n')
    f.write("<link rel='stylesheet' href='https://raw.githubusercontent.com/trh4ckn0n/work/refs/heads/main/style.css'>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<p data-text='TRHACKNON'>TRHACKNON</p>\n")
    f.write("<h1>Liste des Repositories GitHub</h1>\n")
    
    if repos:
        f.write("<table>\n")
        f.write("<thead><tr><th>Nom</th><th>Description</th><th>URL</th><th>Langage</th></tr></thead>\n")
        f.write("<tbody>\n")

        # Remplir le tableau avec les données des repositories
        for repo in repos:
            name = repo.get("name")
            description = repo.get("description", "Pas de description")
            html_url = repo.get("html_url")
            language = repo.get("language", "Inconnu")
            
            f.write(f"<tr><td>{name}</td><td>{description}</td><td><a href='{html_url}' target='_blank'>Voir</a></td><td>{language}</td></tr>\n")
        
        f.write("</tbody>\n")
        f.write("</table>\n")
    else:
        f.write("<p>Aucun repository trouvé.</p>\n")
    
    f.write("<script  src='https://raw.githubusercontent.com/trh4ckn0n/work/refs/heads/main/script.js'></script>\n")
    f.write("</body>\n")
    f.write("</html>\n")

print("README.html généré avec succès.")
