# client side 
# TCP version { connent , wait }

from socket import *

SERVER_IP     = '192.168.1.4'
SERVER_PORT   = 15000

# setting up client socket 
CLIENT_SOCK = socket(  AF_INET , SOCK_STREAM )
CLIENT_SOCK.connect( ( SERVER_IP , SERVER_PORT ) )

# take input from client 
messege = input( "Please input your messege :: " )
encoded_messege = messege.encode()

# send to client 
CLIENT_SOCK.send( encoded_messege )

# recive respond 
modified_messge = CLIENT_SOCK.recv(2048)
decoded_modified_messge = modified_messge.decode()

# print 
print ( "Messege before server processing ::: " , messege )
print ( "Messege after  server processing ::: " , decoded_modified_messge )

# close 
CLIENT_SOCK.close()
