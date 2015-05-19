# Python-Pizza-Protocol
A simple python implementation of a Pizza Ordering system

How to Run:

First run the PizzaServer.py file.
Then run the PizzaClient.py file.

On the client, press 1 in order to see the server's menu. The server will send a string of 3 menu items, each labeled with a number.

In order to make an order on the client start the command with 3 then type the number of the pizza that you want (the number is indicated in the menu that the server sends to the client when the client presses 1), follow this number with a comma and the number of the pizza that you want.

Example input and output from the Client:

Enter Command:

Input: 1

Output: 2 1 Veggie Supreme $12.99 
  2 Meat Lovers $13.99
  3 Volcano Hawaiaan $14.99
  
menuTest.py, menuItemTest.py, and orderTest.py are Unit Tests that checks if each of the helper classes are implemented correctly.

