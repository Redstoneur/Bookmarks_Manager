###############################################################################################
##### Import ##################################################################################
###############################################################################################

import unittest

import main


###############################################################################################
##### Classes #################################################################################
###############################################################################################

# Test class for the Debug class
class TestDebug(unittest.TestCase):
    # Test for the __call__ method
    def test_call(self):
        debug = main.Debug(True)
        # The __call__ method returns nothing, so we check if it is None
        self.assertIsNone(debug("Test message"))

    # Test for the __str__ method
    def test_str(self):
        debug = main.Debug(True)
        # We check if the string representation is correct
        self.assertEqual(str(debug), "debug(True)")


# Test class for the Favorite_Link class
class TestFavoriteLink(unittest.TestCase):
    # Test for the __str__ method
    def test_str(self):
        link = main.Favorite_Link("Title", "URL", "Folder")
        expected_str = "Title: Title\nURL: URL\nFolder: Folder"
        # We check if the string representation is correct
        self.assertEqual(str(link), expected_str)

    # Test for the __dict__ method
    def test_dict(self):
        link = main.Favorite_Link("Title", "URL", "Folder")
        expected_dict = {"Title": "Title", "URL": "URL", "Folder": "Folder"}
        # We check if the dictionary representation is correct
        self.assertEqual(link.__dict__(), expected_dict)

    # Test for the __list__ method
    def test_list(self):
        link = main.Favorite_Link("Title", "URL", "Folder")
        expected_list = ["Title", "URL", "Folder"]
        # We check if the list representation is correct
        self.assertEqual(link.__list__(), expected_list)


###############################################################################################
##### Main ####################################################################################
###############################################################################################

# Run the tests
if __name__ == '__main__':
    unittest.main()
