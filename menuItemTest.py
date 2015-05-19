import unittest
from menuItem import menuItem

class menuItemTest(unittest.TestCase):

    def test_constructor(self):
        """
        Tests if menu item correctly initializes each of the three parameters
        """
        item = menuItem(3, "Veggie Supreme", 12.95)
        self.assertEquals(item.itemNum,3)
        self.assertEquals(item.itemDescription, "Veggie Supreme")
        self.assertEquals(item.itemPrice, 12.95)

    def test_encode(self):
        """
        Tests encode to see if it correctly converts menuItem to string
        """
        item = menuItem(3, "Veggie Supreme", 12.95)
        self.assertEquals(item.encode(), "3 Veggie Supreme $12.95")

if __name__ == '__main__':
    unittest.main()
