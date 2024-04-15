"""
This module contains the main code of the program.
"""

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
    Debugging class to display debug messages.

    Attributes:
        boolean: bool -> A boolean to enable or disable debug mode.
    """
    boolean: bool = False

    def __init__(self, boolean: bool = False) -> None:
        """
        Initializes a new instance of the Debug class.
        :param boolean: A boolean to enable or disable debug mode.
        """
        self.boolean = boolean

    def __call__(self, message: str) -> None:
        """
        Displays a debug message.
        :param message: The debug message to display.
        :return: None
        """
        if self.boolean:
            print(message, file=sys.stderr, flush=True)

    def __str__(self) -> str:
        """
        Returns a string representing the instance of the Debug class.
        :return: A string representing the instance of the Debug class.
        """
        return f"debug({self.boolean})"


class FavoriteLink:
    """
    Class representing a favorite (link) with a title, a URL and a folder.

    Attributes:
        Title: str -> The title of the favorite.
        URL: str -> The URL of the favorite.
        Folder: str -> The folder of the favorite.
    """
    Title: str
    URL: str
    Folder: str

    def __init__(self, title: str, url: str, folder: str = "") -> None:
        """
        Initializes a new instance of the Favorite_Link class.
        :param title: Title of the favorite.
        :param url: URL of the favorite.
        :param folder: Folder of the favorite.
        """
        self.Title = title
        self.URL = url
        self.Folder = folder

    def __str__(self) -> str:
        """
        Returns a string representing the instance of the Favorite_Link class.
        :return: A string representing the instance of the Favorite_Link class.
        """
        return f"Title: {self.Title}\n" \
               f"URL: {self.URL}\n" \
               f"Folder: {self.Folder}"

    def __dict__(self) -> dict:
        """
        Returns a dictionary representing the instance of the Favorite_Link class.
        :return: A dictionary representing the instance of the Favorite_Link class.
        """
        return {
            "Title": self.Title,
            "URL": self.URL,
            "Folder": self.Folder
        }

    def __list__(self) -> list:
        """
        Returns a list representing the instance of the Favorite_Link class.
        :return: A list representing the instance of the Favorite_Link class.
        """
        return [
            self.Title,
            self.URL,
            self.Folder
        ]


###############################################################################################
##### Global Variables ########################################################################
###############################################################################################

debug: Debug = Debug(False)


###############################################################################################
##### Functions ###############################################################################
###############################################################################################

def generate_csv(file: str) -> (bool, str):
    """
    Converts an HTML file of favorites into a CSV file.
    :param file: The HTML file of favorites to convert.
    :return:    A tuple containing a boolean indicating whether the conversion was
                successful and the name of the CSV file.
    """
    # check if the file exists and is accessible
    debug(f"Checking if the file {file} exists and is accessible.")
    try:
        with open(file, "r", encoding="utf-8") as f:
            pass
    except FileNotFoundError:
        print(f"The file {file} does not exist.")
        return False
    except PermissionError:
        print(f"You do not have permission to access the file {file}.")
        return False
    except Exception as e:
        print(f"An error occurred when accessing the file {file}: {e}")
        return False

    # Check if the file is an HTML file
    debug(f"Checking if the file {file} is an HTML file.")
    if not file.endswith(".html"):
        print("The file is not an HTML file.")
        return False

    # retrieve the file name without the extension
    file_name: str = file.split(".")[0]

    # Read the exported bookmarks HTML file
    debug(f"Reading the file {file}.")
    with open(file, "r", encoding="utf-8") as f:
        html_data: str = f.read()

    # Check if the file is empty
    if html_data == "":
        print("The file is empty.")
        return False

    # Parse the HTML file with BeautifulSoup
    soup: BeautifulSoup = BeautifulSoup(html_data, "html.parser")

    # Retrieve all the links (favorites) in the HTML file
    links: list = soup.find_all("a")

    # Create a list of dictionaries to store the favorites data
    favorites_data: list = []

    # Go through the links to extract the favorites and their folders
    debug("Extracting the favorites and their folders.")
    for link in links:

        # Make sure the link is a favorite
        if link.get("add_date") is not None:

            # Go through the favorite's parent tags (folders) to retrieve the full folder path
            folders: list = []
            for parent in link.parents:
                if parent.name == "dl":
                    # Check if the "h3" tag is a folder
                    if parent.find_previous_sibling("h3") is not None:
                        folder: str = parent.find_previous_sibling("h3").text
                        folders.append(folder)

            folders = [folder for folder in folders if folder != ""]
            path: str = " > ".join(folders[::-1])

            favorite: FavoriteLink = FavoriteLink(
                title=link.text,
                url=link.get("href"),
                folder=path
            )
            # noinspection PyTypeChecker
            debug(favorite)
            favorites_data.append(favorite.__dict__)

    # Create a pandas DataFrame from the favorites data
    df = pd.DataFrame(favorites_data)

    # Save the DataFrame in CSV format
    df.to_csv(f"{file_name}.csv", index=False)

    return True, f"{file_name}.csv"


###############################################################################################
##### Main ####################################################################################
###############################################################################################

def main() -> bool:
    """
    Main function of the program.
    """

    program_name: str = "Converter html bookmarks to csv"
    program_version: str = "1.0"
    program_description: str = "Converts an HTML file containing bookmarks to a CSV file."

    # Create an argument parser
    parser = argparse.ArgumentParser(prog=program_name, description=program_description)
    parser.add_argument("file", type=str, help="The HTML file containing the bookmarks to convert.")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {program_version}")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    args = parser.parse_args()

    # Enable debug mode if the option is enabled
    if args.debug:
        global debug
        debug = Debug(True)
        debug(f"Debug mode enabled: {debug}")

    # Convert the bookmarks HTML file into a CSV file
    boolean, file = generate_csv(args.file)
    if boolean:
        print(f"Conversion completed. The favorites have been saved in the file {file}.")
        return True
    print("An error occurred during the conversion of the favorites.")
    return False


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
