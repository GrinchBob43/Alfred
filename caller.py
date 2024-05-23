import socket
newSocket = socket.socket(socket_family, socket_type)


run = False
while run == False:

    if input("What's up? ") == 'get stuff from api':
        run = True
    else:
        print("I am stupid and don't understand that")
while run == True:
