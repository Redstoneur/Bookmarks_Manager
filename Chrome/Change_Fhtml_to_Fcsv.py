import sys
import pandas as pd
from bs4 import BeautifulSoup


class Debug:
    booleen: bool = False

    def __init__(self, booleen: bool = False) -> None:
        self.booleen = booleen

    def __call__(self, message: str) -> None:
        if self.booleen:
            print(message, file=sys.stderr, flush=True)

    def __str__(self) -> str:
        return f"debug({self.booleen})"


class Favorite_Link:
    Title: str
    URL: str
    Folder: str

    def __init__(self, title: str, url: str, folder: str = "") -> None:
        self.Title = title
        self.URL = url
        self.Folder = folder

    def __str__(self) -> str:
        return f"Title: {self.Title}\n" \
               f"URL: {self.URL}\n" \
               f"Folder: {self.Folder}"

    def __dict__(self) -> dict:
        return {
            "Title": self.Title,
            "URL": self.URL,
            "Folder": self.Folder
        }

    def __list__(self) -> list:
        return [
            self.Title,
            self.URL,
            self.Folder
        ]


debug: Debug = Debug(False)  # TODO: Change to False for production and True for debug

# Lisez le fichier HTML des favoris exportés
with open("mes_favoris.html", "r", encoding="utf-8") as file:
    html_data: str = file.read()

# Analysez le fichier HTML avec BeautifulSoup
soup: BeautifulSoup = BeautifulSoup(html_data, "html.parser")

# Récupérez tous les liens (favoris) dans le fichier HTML
links: list = soup.find_all("a")

# Créez une liste de dictionnaires pour stocker les données des favoris
favorites_data: list = []

# Parcourez les liens pour extraire les favoris et leurs dossiers
for link in links:

    # Parcourez les balises parentes (dossiers) du favori pour récupérer le chemin du dossier complet
    folders: list = []
    for parent in link.parents:
        if parent.name == "dl":
            folder: str = parent.find_previous_sibling("h3").text if parent.find_previous_sibling("h3") else ""
            folders.append(folder)
    debug(f"folders1 : {folders}") # Ligne de débogage

    folders = [folder for folder in folders if folder != ""]
    debug(f"folders2 : {folders}") # Ligne de débogage

    path: str = " > ".join(folders[::-1])
    debug(f"path : {path}") # Ligne de débogage

    favorite: Favorite_Link = Favorite_Link(
        title=link.text,
        url=link.get("href"),
        folder=path
    )
    debug(f"favorite.__dict__() :\n{favorite.__dict__()}\n----------\n")  # Ligne de débogage

    favorites_data.append(favorite.__dict__())

# Créez un DataFrame pandas à partir des données des favoris
df = pd.DataFrame(favorites_data)

# Enregistrez le DataFrame au format CSV
df.to_csv("mes_favoris.csv", index=False)

print("Conversion terminée. Les favoris ont été enregistrés dans mes_favoris.csv.")
