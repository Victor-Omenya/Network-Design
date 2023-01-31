#Nishchay Ballupet Neelakantappa
#02041413

#Program for Client side

import socket #importing socket library

Udp_IP = "127.0.0.1" #standard address for IPv4 loopback traffic
Udp_PORT = 12000 #a communications protocol for the Internet network layer, transport layer, and session layer

data = input("input lowercase sentence: ").encode() #encoded the data to be read in bit format

Clientsock = socket.socket(socket.AF_INET, # for Internet
                     socket.SOCK_DGRAM) # for UDP

Clientsock.sendto(data, (Udp_IP, Udp_PORT)) #for sending datagram message
Modified_data, Server_addr = Clientsock.recvfrom(2048) #for receiving datagram message
print("\n The server responded back:", Modified_data.decode(), "\n") 
Clientsock.close() #close after receving