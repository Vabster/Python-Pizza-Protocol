import unittest
from menuItem import menuItem
from menu import menu

class menuTest(unittest.TestCase):
    """
    Tests the constructor and methods of the menu class
    """
    def test_constructor(self):
        """
        Checks if menu initializes menuList
        """
        testMenu = menu()
        self.assertEquals(testMenu.menuList, [])

    def test_encodeMenu(self):
        """
        Tests if encodeMenu correctly converts a menu to string form
        """
        testMenu = menu()
        item1 = menuItem(1, "Veggie", 12.95)
        item2 = menuItem(2, "Meat", 11.95)
        testMenu.add(item1)
        testMenu.add(item2)

        correctString = "1 Veggie $12.95\n  2 Meat $11.95"
        self.assertEquals(testMenu.encodeMenu(), correctString)



if __name__ == '__main__':
    unittest.main()

