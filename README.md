# drawsForInstagram

A basic program that receives a text with this pattern:


username1,1: @ username1,2 @ username1,3 ... @ username1, N

username2,1: @ username2,2 @ username2,3 ... @ username2, N
.
.
usernameN, 1: @ usernameN, 2 @ usernameN, 3 ... @ usernameN,N


The program outputs a vector with (username1,1; username2,1; ...; usernameN, 1)

If some usernameI, J is the same than another, then the program outputs only one time the username, next to a number that indicates how many times the usernameI, J appears
