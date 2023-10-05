from pychrome import PyChrome
import csv

# Chemin d'accès au fichier CSV contenant les favoris
csv_file = "mes_favoris.csv"

# Créez une instance de PyChrome
chrome = PyChrome()

# Lisez le fichier CSV
with open(csv_file, "r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        title = row["Titre"]
        url = row["URL"]

        # Ajoutez le favori à Google Chrome dans le dossier spécifié
        chrome.add_bookmark(title, url, folder="Mes Favoris Importés")

# Fermez l'instance de PyChrome
chrome.close()

print("Importation des favoris dans le dossier spécifié terminée.")
