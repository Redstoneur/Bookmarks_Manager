# Bookmarks Manager

![License](https://img.shields.io/github/license/Redstoneur/Bookmarks_Manager)
![Top Language](https://img.shields.io/github/languages/top/Redstoneur/Bookmarks_Manager)
![Build Status](https://img.shields.io/github/actions/workflow/status/Redstoneur/Bookmarks_Manager/build-and-publish.yml)
![Latest Release](https://img.shields.io/github/v/release/Redstoneur/Bookmarks_Manager)
![Release Date](https://img.shields.io/github/release-date/Redstoneur/Bookmarks_Manager)
![Last Commit](https://img.shields.io/github/last-commit/Redstoneur/Bookmarks_Manager)

Bookmarks Manager is a Python program that converts an HTML file containing bookmarks into a CSV file. It was designed to facilitate the management and organization of bookmarks.

## Operation
The program takes an HTML file containing bookmarks (usually exported from a web browser) as input and generates a CSV file containing these bookmarks. Each bookmark is represented by a line in the CSV file, with columns for the bookmark's title, URL, and folder.

## Usage

To retrieve the program, you can clone this repository using the following command:

```bash
git clone https://github.com/Redstoneur/Bookmarks_Manager.git Bookmarks_Manager
cd Bookmarks_Manager
```

To use the program, you must first install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
```

Then, you can run the program using the following command:

```bash
python main.py <path_to_HTML_file>
```

Replace `<path_to_HTML_file>` with the path to the HTML file containing your bookmarks.

## License

This program is distributed under the GNU General Public License v3.0. For more information, please refer to the `LICENSE` file included with this program.