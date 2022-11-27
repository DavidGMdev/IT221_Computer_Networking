# server side 
# TCP version { lisen , wait , accept }

from socket import *

SERVER_IP     = '192.168.1.4'
SERVER_PORT   = 15000

# creating server socket , data base TCP socket Stream type 
SERVER_SOCKT = socket ( AF_INET , SOCK_STREAM )
SERVER_SOCKT.bind ( ( '' , SERVER_PORT ) )

# tcp listining 
SERVER_SOCKT.listen(1)

# welcome 
print( f"Starting server  [{SERVER_IP}] , [{SERVER_PORT}] ::: ")

# responding 
while True :
    
    # accept client request 
    connection_Socket , client_address = SERVER_SOCKT.accept()

    # recive data
    messege = connection_Socket.recv(2048)
    decoded_messege = messege.decode()
    
    # do process 
    modified_messege = decoded_messege.upper() 
    encoded_modified_messege = modified_messege.encode()

    #send respond 
    connection_Socket.send ( encoded_modified_messege )

    # print this respond details 
    print ( f"Responding to :: {client_address} ")
    print ( f"Recived from the client :: {decoded_messege} ")
    print ( f"Respond from the server :: {modified_messege} ")
    
    #connection_Socket.close()
    print()
    print()
    print ( f"[{SERVER_IP}] , [{SERVER_PORT}] server Listening  :::")


