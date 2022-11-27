# clinet side script 
# UDP tecnique connection 

from socket import *

# server constants 
SERVER_IP   = '192.168.1.4'
SERVER_PORT = 11000

# client UDP socket
CLIENT_SOCK = socket( AF_INET , SOCK_DGRAM )
CLIENT_SOCK.bind( ('' , 0 ) )

connect = 'yes'

while ( connect != 'exit' ) :
    
    # TAKE CLEINT DATA
    message = input ( 'Please , Enter Your Messege :: ' )
    connect = message

    if connect != 'exit' :
        # sending 
        CLIENT_SOCK.sendto( message.encode() , ( SERVER_IP , SERVER_PORT ) )

        # reciving 
        modified_message , server_address = CLIENT_SOCK.recvfrom(2048)
        modified_message = modified_message.decode() 

        # print info 
        print ( "Messege before server processing ::: " , message )
        print ( "Messege after  server processing ::: " , modified_message )
        
    else :
        
        #close connection 
        CLIENT_SOCK.close()
