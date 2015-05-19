class menuItem:
    """ Represents a single menu item, that stores the item number, the description of the item and the prie of the item """

    def __init__(self, itemNum, itemDescription, itemPrice):
        """
        Creates a menu item using the constructor parameters
        :param itemNum: Order number
        :param itemDescription: Type of pizza
        :param itemPrice: Price of pizza
        """
        # Constructor, initializes each of the item number, description, and price to their corresponding parameters
        self.itemNum = itemNum
        self.itemDescription = itemDescription
        self.itemPrice = itemPrice

    def encode(self):
        """
        Turns menuItem into string variable
        :return: String version of menu item
        """
        encode = str(self.itemNum) + " " + str(self.itemDescription) + " $" + str(self.itemPrice)
        return encode

    def getitemPrice(self):
        """
        :return: The price of the item is returned
        """
        return self.itemPrice





