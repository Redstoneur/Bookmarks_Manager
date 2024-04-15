import unittest
import main

# Classe de test pour la classe Debug
class TestDebug(unittest.TestCase):
    # Test pour la méthode __call__
    def test_call(self):
        debug = main.Debug(True)
        # La méthode __call__ ne retourne rien, donc on vérifie si elle est None
        self.assertIsNone(debug("Test message"))

    # Test pour la méthode __str__
    def test_str(self):
        debug = main.Debug(True)
        # On vérifie si la représentation en chaîne de caractères est correcte
        self.assertEqual(str(debug), "debug(True)")

# Classe de test pour la classe Favorite_Link
class TestFavoriteLink(unittest.TestCase):
    # Test pour la méthode __str__
    def test_str(self):
        link = main.Favorite_Link("Title", "URL", "Folder")
        expected_str = "Title: Title\nURL: URL\nFolder: Folder"
        # On vérifie si la représentation en chaîne de caractères est correcte
        self.assertEqual(str(link), expected_str)

    # Test pour la méthode __dict__
    def test_dict(self):
        link = main.Favorite_Link("Title", "URL", "Folder")
        expected_dict = {"Title": "Title", "URL": "URL", "Folder": "Folder"}
        # On vérifie si la représentation en dictionnaire est correcte
        self.assertEqual(link.__dict__(), expected_dict)

    # Test pour la méthode __list__
    def test_list(self):
        link = main.Favorite_Link("Title", "URL", "Folder")
        expected_list = ["Title", "URL", "Folder"]
        # On vérifie si la représentation en liste est correcte
        self.assertEqual(link.__list__(), expected_list)

# Exécution des tests
if __name__ == '__main__':
    unittest.main()