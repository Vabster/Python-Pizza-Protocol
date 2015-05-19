from socket import gethostbyname
import socket

""" Takes user input, sends it to the server, and receives message back """
# Gets the server host
hostName = socket.gethostbyname(socket.gethostname())
# Sets port to 2014
port = 2014

# Creates client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initial prompt of user
print "Enter command"

while True:
    """ Takes a line of user input and sends it to server and then reads the response from server """
    # Takes input from user
    message = raw_input()
    # Sends user input to server
    clientSocket.sendto(message,(hostName, port))
    # Receives message back from server
    serverResponse, server = clientSocket.recvfrom(1024)
    # Prints message from server
    print serverResponse
    # Ends program if user types in 'quit'

clientSocket.close()

