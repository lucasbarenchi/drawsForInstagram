# drawsForInstagram

A basic program that receives a text with this pattern:

...
username1,1: @ username1,2 @ username1,3 ... @ username1, N \ n
..
..
..
usernameN, 1: @ usernameN, 2 @ usernameN, 3 ... @ usernameN, 4 \ n
...

The program outputs a vector with (username1,1; username2,1; ...; usernameN, 1)

If some usernameI, J is the same than another, then the program outputs only one time the username, next to a number that indicates how many times the usernameI, J appears
