# Gestionnaire de Favoris

![License](https://img.shields.io/github/license/Redstoneur/Gestionaire_Favoris)
![Top Language](https://img.shields.io/github/languages/top/Redstoneur/Gestionaire_Favoris)
![Build Status](https://img.shields.io/github/actions/workflow/status/Redstoneur/Gestionaire_Favoris/build-and-publish.yml)
![Latest Release](https://img.shields.io/github/v/release/Redstoneur/Gestionaire_Favoris)
![Release Date](https://img.shields.io/github/release-date/Redstoneur/Gestionaire_Favoris)
![Last Commit](https://img.shields.io/github/last-commit/Redstoneur/Gestionaire_Favoris)

Gestionnaire de Favoris est un programme Python qui convertit un fichier HTML contenant des favoris en un fichier CSV. Il a été conçu pour faciliter la gestion et l'organisation des favoris.

## Fonctionnement

Le programme prend en entrée un fichier HTML contenant des favoris (généralement exporté depuis un navigateur web) et génère un fichier CSV contenant ces favoris. Chaque favori est représenté par une ligne dans le fichier CSV, avec des colonnes pour le titre, l'URL et le dossier du favori.

## Utilisation

Pour récupérer le programme, vous pouvez cloner ce dépôt en utilisant la commande suivante :

```bash
git clone https://github.com/Redstoneur/Gestionaire_Favoris.git Gestionaire_Favoris
cd Gestionaire_Favoris
```

Pour utiliser le programme, vous devez d'abord installer les dépendances nécessaires en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

Ensuite, vous pouvez exécuter le programme en utilisant la commande suivante :

```bash
python main.py <chemin_vers_le_fichier_HTML>
```

Remplacez `<chemin_vers_le_fichier_HTML>` par le chemin vers le fichier HTML contenant vos favoris.

## Licence

Ce programme est distribué sous la licence GNU General Public License v3.0. Pour plus d'informations, veuillez consulter le fichier `LICENSE` inclus avec ce programme.
