"""
This module contains unit tests for the main module.
"""

###############################################################################################
##### Import ##################################################################################
###############################################################################################

import unittest

import main


###############################################################################################
##### Classes #################################################################################
###############################################################################################
class TestDebug(unittest.TestCase):
    """
    Test class for the Debug class in the main module.
    """

    def test_call(self):
        """
        Test for the __call__ method of the Debug class.
        """
        debug = main.Debug(True)
        self.assertIsNone(debug("Test message"))

    def test_str(self):
        """
        Test for the __str__ method of the Debug class.
        """
        debug = main.Debug(True)
        self.assertEqual(str(debug), "debug(True)")


class TestFavoriteLink(unittest.TestCase):
    """
    Test class for the Favorite_Link class in the main module.
    """

    def test_str(self):
        """
        Test for the __str__ method of the Favorite_Link class.
        """
        link = main.FavoriteLink("Title", "URL", "Folder")
        expected_str = "Title: Title\nURL: URL\nFolder: Folder"
        self.assertEqual(str(link), expected_str)

    def test_dict(self):
        """
        Test for the __dict__ property of the Favorite_Link class.
        """
        link = main.FavoriteLink("Title", "URL", "Folder")
        expected_dict = {"Title": "Title", "URL": "URL", "Folder": "Folder"}
        self.assertEqual(link.__dict__, expected_dict)

    def test_list(self):
        """
        Test for the __list__ method of the Favorite_Link class.
        """
        link = main.FavoriteLink("Title", "URL", "Folder")
        expected_list = ["Title", "URL", "Folder"]
        self.assertEqual(link.__list__(), expected_list)


###############################################################################################
##### Main ####################################################################################
###############################################################################################

# Run the tests
if __name__ == '__main__':
    unittest.main()
