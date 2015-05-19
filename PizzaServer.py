from socket import *
import re
from menuItem import menuItem
from menu import menu
from order import order

class PizzaServer:
    """
    UDP Server that either sends menu, total amount owed, or an error message to the client
    """
    def responseTo(self, message, pizzaMenu):
        """
        Sends a response back to client based on the input received from the client
        :param message: The message from the client
        :param pizzaMenu: a hardcoded menu established later
        :return: a string response that will be send to the client
        """
        # Try statement protects against empty message sent from client
        try:
            # If message is 1, sends the menu to the client
            if message == "1":
                # Creates the string that will be sent back to the client
                menuString = pizzaMenu.encodeMenu()
                menu = "2 " + menuString
                print "Menu Request"
                return menu
            # Enters this statement if input form client begins with 3
            elif message[0] == "3":
                print "Confirmation"
                # Creates order object that will parse the user input
                orderFormat = order()

                # Determines if user order input is in proper format, and if it isn't then send an error message back
                if(orderFormat.orderFormatCheck(message) == False):
                    # Send error message to user
                    return "5 1 Malformed Message for order message"

                # Each number in client order is separated into a list
                decodeOrder = orderFormat.stripOrder(message)

                # Creates item list which, contains the item number for each pizza ordered by client
                itemList = decodeOrder[::2]
                # Creates list which contains the amount of each pizza the client ordered
                amountList = decodeOrder[1::2]
                # Sets price to 0
                price = 0

                for a in range(len(amountList)):
                    """ Increments price by itemList[a] * amountList[a],
                    returns error if user orders menu item that does not exist
                    """
                    # Checks if item bought is part of menu item list
                    if(itemList[a] > len(pizzaMenu.priceList)):
                        return "5 2 Item not available, type 1 to see our menu"
                    # Increases price
                    price = price  + (pizzaMenu.priceList[itemList[a] - 1] * amountList[a])
                else:
                    # Enters here if for closes naturally
                    return "4 $" + str(price)
            else:
                return "5 1 Malformed Message"
        except:
            return "5 1 Malformed Message"

""" UDP Server """
""" Waits for response from client and echos client response back to the client """
# Sets port number to 2014
port = 2014
# Creates the server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Creates menu and adds items to the menu
pizzaMenu = menu()
item1 = menuItem(1, "Veggie Supreme", 12.99)
pizzaMenu.add(item1)
item2 = menuItem(2, "Meat Lovers", 13.99)
pizzaMenu.add(item2)
item3 = menuItem(3, "Volcano Hawaiian", 14.99)
pizzaMenu.add(item3)

# Binds host name ('' means machine name) to port
serverSocket.bind(('', port))
# Lets user know server has started
print "Server is on:"

while True:
    """ Receives a one line message from client and based on input sends a message back to client """
    # Takes input from client
    message, client = serverSocket.recvfrom(1024)
    # Creates server class object
    serverMethod = PizzaServer()
    # Gets response from repsonseTo method
    response = serverMethod.responseTo(message, pizzaMenu)
    # Sends response to the client
    serverSocket.sendto(response, client)
