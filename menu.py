from menuItem import menuItem

class menu:
    """
    Menu class that stores multiple menu items
    """
    def __init__(self):
        """
        Constructor initializes menuList and priceList
        """
        self.menuList = []
        self.priceList = []

    def add(self, item):
        """
        Adds an item to menuList and priceList
        :param item: a menuItem object
        """
        self.menuList.append(item)
        self.priceList.append(item.getitemPrice())

    def encodeMenu(self):
        """
        Encodes entire menu into a string variable
        :return: string version of the menu
        """
        encoding = ""
        for item in range(len(self.menuList)):
            """ Adds an encoded menuItem to the encoding string """
            if item == len(self.menuList) - 1:
                encoding += self.menuList[item].encode()
            else:
                encoding += self.menuList[item].encode() +'\n  '
        return encoding





