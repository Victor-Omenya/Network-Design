#Nishchay Ballupet Neelakantappa
#02041413

#Program for Server side

import socket #importing socket library

Udp_IP = "127.0.0.1" #standard address for IPv4 loopback traffic
Udp_PORT = 12000 #a communications protocol for the Internet network layer, transport layer, and session layer

Serversock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

Serversock.bind((Udp_IP, Udp_PORT)) #bind the server socket to the local host and port
print("The server is up and ready to receive \n")

#infinite while loop to keep talking with the client 
while True:
    data, CLaddr = Serversock.recvfrom(2048) ##for receiving datagram message
    print("Client says: %s" %data, '\n') #pring the received message
    Modified_data= data.decode().upper() #Modify the received data to upper case
    Serversock.sendto(Modified_data.encode(), CLaddr) #encode the modified data to bit format and send it to the client
    
   
    

    
