# server side script 
# UDP tecnique connection 

from socket import *

# server constants 
SERVER_PORT = 11000
SERVER_IP   = '192.168.1.4'

# server UDP socket
SERVER_SOCK = socket( AF_INET , SOCK_DGRAM )
SERVER_SOCK.bind( ('' , SERVER_PORT ) )

# on having server ready to recive 
print ( f"[{SERVER_IP}] , [{SERVER_PORT}] is now ready to respond to clients ::" )

# server respond to client 
while True :
    
    # recive client data 
    message , client_address = SERVER_SOCK.recvfrom(2048)

    #server process
    modified_message = message.upper()

    # decode messege
    modified_message = modified_message.decode()

    # sending the results back
    SERVER_SOCK.sendto ( modified_message.encode() , client_address )

    #print deatils about each respond 
    print ( f"Responding to :: {client_address} ")
    print ( f"Recived from the client :: {message.decode()} ")
    print ( f"Respond from the server :: {modified_message} ")

