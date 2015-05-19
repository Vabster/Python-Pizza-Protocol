import re
class order:
    """ Determines if an order command from the user is in the correct format """

    def orderFormatCheck(self, orderString):
        """
        :param orderString: order command sent from client, begins with a '3'
        :return: True if in correct order format, and false otherwise
        """
        orderRegExp = re.compile("^([0-9]+,[0-9]+ )*([0-9]+,[0-9]+)$")
        # Creates String with all input from client besides the beginning 3
        decodeOrder = orderString[1:]
        # Removes spaces from before or after the first char
        decodeOrder = decodeOrder.strip()
        if(orderRegExp.match(decodeOrder) == None):
            return False
        else:
            return True

    def stripOrder(self, orderString):
        """
        Makes client message into list stripped of commas
        :param orderString: Client message to be stripped and made into list
        :return: list based on client message
        """
        # Creates String with all input from client besides the beginning 3
        decodeOrder = orderString[1:]
        # Removes spaces from before or after the first char
        decodeOrder = decodeOrder.strip()
        # Removes comma from decodeOrder and makes it into a list
        decodeOrder = decodeOrder.replace(',', ' ').split(" ")
        # Makes each element in decode order an integer
        decodeOrder = [int(i) for i in decodeOrder]
        return decodeOrder
