# Author and Title:  
Title: Design File for Phase 3  

Group 6 Members:  
Victor  
Samonorom  
Adarsh  
Nishchay  

# Purpose of The Phase:  
Purpose of Phase 3 is...

# Code Explanation:  


# BEGINNING OF EXAMPLE  
----------------------------------------------------  

## serverUDP.py  
### 1.	serverUDP.py Library and Parameter Setup:  

    # Import socket and time library  
    import socket  
    import time  

    # Configuration parameters for server  
    UDP_IP = "localhost"    \# Could use "127.0.0.1"  
    UDP_PORT = 8080         \# Assigned port # to communicate  
    PACKET_SIZE = 2048      \# Size of each packet to send (can be adjusted)  
    SLEEP_TIME = 1          \# Intervals to prevent overloading  

a.	On “serverUDP.py”, first, two libraries are imported (socket and time). Socket is to allow for communications through the network, and time allows us to use intervals to prevent bottleneck. This is done using “import socket” and “import time”.  
b.	Next, parameters are setup. First, using “localhost” allow us to get the machine’s local IP address, but using “127.0.0.1” would also work due to it being the home IP address. Either one is used to assign the machine’s IP address to UDP_IP.   
c.	UDP_PORT is used to assign a port number to allow direct communication between the client and server.  
d.	PACKET_SIZE is used to determine how many bits will each packet contain. The size can be changed to the user preference, but the larger the packet size, the slower the transfer speed will be.  
e.	SLEEP_TIME is used as a 1 second interval for another function to prevent bottleneck on the server while transferring the packets.  

  # ENDING OF EXAMPLE  
----------------------------------------------------  


# Execution Example:  

## 1.	[Title:]  
[Short Description]  

 [Insert Image]  

 

