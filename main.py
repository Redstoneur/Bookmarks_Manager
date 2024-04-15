###############################################################################################
##### Import ##################################################################################
###############################################################################################

import argparse
import sys

import pandas as pd
from bs4 import BeautifulSoup


###############################################################################################
##### Classes #################################################################################
###############################################################################################


class Debug:
    """
    Classe de débogage pour afficher des messages de débogage.

    Attributes:
        booleen: bool -> Un booléen pour activer ou désactiver le mode de débogage.
    """
    booleen: bool = False

    def __init__(self, booleen: bool = False) -> None:
        """
        Initialise une nouvelle instance de la classe Debug.
        :param booleen: Un booléen pour activer ou désactiver le mode de débogage.
        """
        self.booleen = booleen

    def __call__(self, message: str) -> None:
        """
        Affiche un message de débogage.
        :param message: Le message de débogage à afficher.
        :return: None
        """
        if self.booleen:
            print(message, file=sys.stderr, flush=True)

    def __str__(self) -> str:
        """
        Retourne une chaîne de caractères représentant l'instance de la classe Debug.
        :return: Une chaîne de caractères représentant l'instance de la classe Debug.
        """
        return f"debug({self.booleen})"


class Favorite_Link:
    """
    Classe représentant un favori (lien) avec un titre, une URL et un dossier.

    Attributes:
        Title: str -> Le titre du favori.
        URL: str -> L'URL du favori.
        Folder: str -> Le dossier du favori.
    """
    Title: str
    URL: str
    Folder: str

    def __init__(self, title: str, url: str, folder: str = "") -> None:
        """
        Initialise une nouvelle instance de la classe Favorite_Link.
        :param title: Titre du favori.
        :param url: URL du favori.
        :param folder: Dossier du favori.
        """
        self.Title = title
        self.URL = url
        self.Folder = folder

    def __str__(self) -> str:
        """
        Retourne une chaîne de caractères représentant l'instance de la classe Favorite_Link.
        :return: Une chaîne de caractères représentant l'instance de la classe Favorite_Link.
        """
        return f"Title: {self.Title}\n" \
               f"URL: {self.URL}\n" \
               f"Folder: {self.Folder}"

    def __dict__(self) -> dict:
        """
        Retourne un dictionnaire représentant l'instance de la classe Favorite_Link.
        :return: Un dictionnaire représentant l'instance de la classe Favorite_Link.
        """
        return {
            "Title": self.Title,
            "URL": self.URL,
            "Folder": self.Folder
        }

    def __list__(self) -> list:
        """
        Retourne une liste représentant l'instance de la classe Favorite_Link.
        :return: Une liste représentant l'instance de la classe Favorite_Link.
        """
        return [
            self.Title,
            self.URL,
            self.Folder
        ]

###############################################################################################
##### Variables Globales ######################################################################
###############################################################################################

debug: Debug = Debug(False)
program_name: str = "Converter html bookmarks to csv"
program_version: str = "1.0"
program_description: str = "Converts an HTML file containing bookmarks to a CSV file."

###############################################################################################
##### Fonctions ###############################################################################
###############################################################################################

def Generate_CSV(file: str) -> (bool, str):
    """
    Convertit un fichier HTML de favoris en un fichier CSV.
    :param file: Le fichier HTML des favoris à convertir.
    :return: Un tuple contenant un booléen indiquant si la conversion a réussi et le nom du fichier CSV.
    """
    global debug

    # vérifier si le fichier existe et est accessible
    try:
        with open(file, "r", encoding="utf-8") as f:
            pass
    except FileNotFoundError:
        print(f"Le fichier {file} n'existe pas.")
        return False
    except PermissionError:
        print(f"Vous n'avez pas la permission d'accéder au fichier {file}.")
        return False
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'accès au fichier {file}: {e}")
        return False

    # Vérifiez si le fichier est un fichier HTML
    if not file.endswith(".html"):
        print("Le fichier n'est pas un fichier HTML.")
        return False

    # récupérer le nom du fichier sans l'extension
    file_name: str = file.split(".")[0]

    # Lisez le fichier HTML des favoris exportés
    with open(file, "r", encoding="utf-8") as f:
        html_data: str = f.read()

    # Vérifiez si le fichier est vide
    if html_data == "":
        print("Le fichier est vide.")
        return False

    # Analysez le fichier HTML avec BeautifulSoup
    soup: BeautifulSoup = BeautifulSoup(html_data, "html.parser")

    # Récupérez tous les liens (favoris) dans le fichier HTML
    links: list = soup.find_all("a")

    # Créez une liste de dictionnaires pour stocker les données des favoris
    favorites_data: list = []

    # Parcourez les liens pour extraire les favoris et leurs dossiers
    for link in links:

        # Assurez-vous que le lien est un favori
        if link.get("add_date") is not None:

            # Parcourez les balises parentes (dossiers) du favori pour récupérer le chemin du dossier complet
            folders: list = []
            for parent in link.parents:
                if parent.name == "dl":
                    # Vérifiez si la balise "h3" est un dossier
                    if parent.find_previous_sibling("h3") is not None:
                        folder: str = parent.find_previous_sibling("h3").text
                        folders.append(folder)

            folders = [folder for folder in folders if folder != ""]
            path: str = " > ".join(folders[::-1])

            favorite: Favorite_Link = Favorite_Link(
                title=link.text,
                url=link.get("href"),
                folder=path
            )
            debug(favorite.__str__())
            favorites_data.append(favorite.__dict__())

    # Créez un DataFrame pandas à partir des données des favoris
    df = pd.DataFrame(favorites_data)

    # Enregistrez le DataFrame au format CSV
    df.to_csv(f"{file_name}.csv", index=False)

    return True, f"{file_name}.csv"


def main() -> bool:
    global debug, program_name, program_version, program_description

    # Créez un analyseur d'arguments
    parser = argparse.ArgumentParser(prog=program_name, description=program_description)
    parser.add_argument("file", type=str, help="The HTML file containing the bookmarks to convert.")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {program_version}")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    args = parser.parse_args()

    # Activez le mode de débogage si l'option est activée
    if args.debug:
        debug = Debug(True)
        debug(f"Mode de débogage activé: {debug}")

    # Convertissez le fichier HTML des favoris en un fichier CSV
    booleen, file = Generate_CSV(args.file)
    if booleen:
        print(f"Conversion terminée. Les favoris ont été enregistrés dans le fichier {file}.")
        return True
    else:
        print("Une erreur s'est produite lors de la conversion des favoris.")
        return False


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
