import sys
import pandas as pd
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

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


class App:
    def __init__(self, root):
        self.label = None
        self.browse_button = None
        self.convert_button = None
        self.status_label = None
        self.file_path = None

        self.root = root
        self.root.title("Conversion de favoris")

        self.debug = Debug(False)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Sélectionnez le fichier HTML des favoris")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(self.root, text="Parcourir", command=self.browse_file)
        self.browse_button.pack(pady=5)

        self.convert_button = tk.Button(self.root, text="Convertir en CSV", command=self.convert_to_csv)
        self.convert_button.pack(pady=10)

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers HTML", "*.html")])
        self.debug(f"Chemin du fichier HTML : {file_path}")
        self.file_path = file_path

    def convert_to_csv(self):
        if hasattr(self, 'file_path') and self.file_path:
            self.status_label.config(text="Conversion en cours...")
            self.root.update()

            # Lire le fichier HTML des favoris exportés
            with open(self.file_path, "r", encoding="utf-8") as file:
                html_data: str = file.read()

            # Analyser le fichier HTML avec BeautifulSoup
            soup: BeautifulSoup = BeautifulSoup(html_data, "html.parser")

            # Récupérer tous les liens (favoris) dans le fichier HTML
            links: list = soup.find_all("a")

            # Créer une liste de dictionnaires pour stocker les données des favoris
            favorites_data: list = []

            # Parcourir les liens pour extraire les favoris et leurs dossiers
            for link in links:
                # Parcourir les balises parentes (dossiers) du favori pour récupérer le chemin du dossier complet
                folders: list = []
                for parent in link.parents:
                    if parent.name == "dl":
                        folder: str = parent.find_previous_sibling("h3").text if parent.find_previous_sibling(
                            "h3") else ""
                        folders.append(folder)
                self.debug(f"folders1 : {folders}")  # Ligne de débogage

                folders = [folder for folder in folders if folder != ""]
                self.debug(f"folders2 : {folders}")  # Ligne de débogage

                path: str = " > ".join(folders[::-1])
                self.debug(f"path : {path}")  # Ligne de débogage

                favorite: Favorite_Link = Favorite_Link(
                    title=link.text,
                    url=link.get("href"),
                    folder=path
                )
                self.debug(f"favorite.__dict__() :\n{favorite.__dict__()}\n----------\n")  # Ligne de débogage

                favorites_data.append(favorite.__dict__())

            # Créer un DataFrame pandas à partir des données des favoris
            df = pd.DataFrame(favorites_data)

            # Enregistrez le DataFrame au format CSV
            df.to_csv("mes_favoris.csv", index=False)

            self.status_label.config(text="Conversion terminée. Les favoris ont été enregistrés dans mes_favoris.csv.")
        else:
            self.status_label.config(text="Sélectionnez un fichier HTML d'abord.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
