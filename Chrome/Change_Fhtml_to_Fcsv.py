import pandas as pd
from bs4 import BeautifulSoup

# Lisez le fichier HTML des favoris exportés
with open("mes_favoris.html", "r", encoding="utf-8") as file:
    html_data = file.read()

# Analysez le fichier HTML avec BeautifulSoup
soup = BeautifulSoup(html_data, "html.parser")

# Récupérez tous les liens (favoris) dans le fichier HTML
links = soup.find_all("a")

# Créez une liste de dictionnaires pour stocker les données des favoris
favorites_data = []

for link in links:
    favorite = {
        "Titre": link.text,
        "URL": link["href"]
    }
    favorites_data.append(favorite)

# Créez un DataFrame pandas à partir des données des favoris
df = pd.DataFrame(favorites_data)

# Enregistrez le DataFrame au format CSV
df.to_csv("mes_favoris.csv", index=False)

print("Conversion terminée. Les favoris ont été enregistrés dans mes_favoris.csv.")
