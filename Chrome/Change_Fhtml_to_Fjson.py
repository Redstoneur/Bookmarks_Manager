import json
from bs4 import BeautifulSoup

def extract_bookmarks_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Trouver toutes les balises 'a' contenant des liens de favoris
    bookmark_links = soup.find_all('a')

    def create_nested_structure(links):
        bookmarks = {"Dossier": {}, "Favoris": []}
        for link in links:
            # Obtenir le chemin du dossier parent du favori
            parent_folders = link.find_all_previous('h3')
            folder_path = '/'.join([folder.text.strip() for folder in parent_folders[::-1]])

            # Créer un dictionnaire pour le favori
            bookmark = {
                "titre": link.text,
                "url": link['href']
            }

            if folder_path:
                # Utiliser la récursivité pour ajouter le favori dans la structure du dossier
                folders = folder_path.split('/')
                current_structure = bookmarks
                for folder in folders:
                    current_structure = current_structure["Dossier"].setdefault(folder, {"Dossier": {}, "Favoris": []})
                current_structure["Favoris"].append(bookmark)
            else:
                # Ajouter le favori directement dans la liste de favoris
                bookmarks["Favoris"].append(bookmark)

        return bookmarks

    return create_nested_structure(bookmark_links)

def save_bookmarks_to_json(bookmarks, json_file):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    html_file = 'mes_favoris.html'  # Remplacez par le chemin de votre fichier HTML de favoris
    json_file = 'favoris_chrome.json'  # Le fichier JSON de sortie

    bookmarks = extract_bookmarks_from_html(html_file)
    save_bookmarks_to_json(bookmarks, json_file)

    print(f"Les favoris ont été enregistrés dans {json_file}.")
