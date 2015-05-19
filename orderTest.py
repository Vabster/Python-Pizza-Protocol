import unittest
from order import order

class orderTest(unittest.TestCase):
    """
    Tests the functions in the order class
    """
    def test_orderFormatCheck(self):
        """
        tests if the format check function returns the correct bool value
        """
        orderCheck = order()
        boolean = orderCheck.orderFormatCheck("3 1,2 3,2")
        self.assertEquals(boolean, True)
        boolean = orderCheck.orderFormatCheck("3 1,2 3,2 4,3,")
        self.assertEquals(boolean, False)
        boolean = orderCheck.orderFormatCheck("3 1")
        self.assertEquals(boolean, False)
        boolean = orderCheck.orderFormatCheck("3 1,,")
        self.assertEquals(boolean, False)

    def test_stripOrder(self):
        """
        tests if the stripOrder function correctly strips order and returns correct list
        """
        orderCheck = order()
        decodedOrder = orderCheck.stripOrder("3 1,2 3,2")

        orderList = [1, 2, 3, 2]
        self.assertEquals(orderList, decodedOrder)

if __name__ == '__main__':
    unittest.main()
