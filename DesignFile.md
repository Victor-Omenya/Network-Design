# Author and Title:  
Title: Design File for Phase 2  

Group 6 Members:  
Victor  
Samonorom  
Adarsh  
Nishchay  

# Purpose of The Phase:  
Purpose is to provide reliable data transfer (RDT) service assuming that the underlying layer is perfectly 
reliable using UDP connection developed or not. An image file will be broken down into packets and be sent from a client to a server.  

# Code Explanation:  

[Code explination.docx](https://github.com/Victor-Omenya/Network-Design/files/10717782/Code.explination.docx)  

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

### 2.	serverUDP.py Socket Setup:  

    # Create a UDP socket for the server  
    Serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

    # Bind the socket to a specific address and port  
    server_address = (UDP_IP, UDP_PORT)  
    Serversock.bind(server_address)  

a.	“Serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)”uses the socket function to create a UDP socket for the client, allowing it to communicate with clients/servers.  
b.	“server_address  = (UDP_IP, UDP_PORT)” and “Serversock.bind(server_address)are used to bind the socket to a specific address and port for communication.  
c.	A print statement will notify the user that the server is ready, indicating that clientUDP.py should be ran next.  

### 3.	serverUDP.py File Receiving Loop:  

    # Print message indicating server is ready, notifying the user to run the client  
    print("Server is ready to receive the image")  
  
    # Open the image file for writing  
    with open("received_image.jpg", "wb") as image_file:  
    while True:  
        # Receive data from the client  
        data, client_address = Serversock.recvfrom(PACKET_SIZE)  
  
        # Write the received data to the image file  
        received_image = image_file.write(data)  
  
        # Print message for each packet received  
        print("A chunk of the image was received as a packet")  

        # Wait for the next Packet of data  
        time.sleep(SLEEP_TIME)  


a.	Using “with open("received_image.jpg", "wb") as image_file:”, the packets being sent from the client to the server will be used to recreate the image into another file named “received_image.jpg”. The command “wb” will write the bits into the new jpg file.  
b.	“data, client_address = Serversock.recvfrom(PACKET_SIZE)” is used to receive the packet from the client.  
c.	“received_image = image_file.write(data)” will write the data to the received_image.jpg file.  
d.	Each time a packet is received, a print statement will notify the user. Indicating more of the image has been sent.  
e.	“time.sleep(SLEEP_TIME)”, will use a 1 second interval to prevent bottleneck.  

## clientUDP.py  
4.	clientUDP.py Library and Parameter Setup:  

        # Import socket and time library  
        import socket  
        import time  

        # Configuration parameters for client  
        UDP_IP = "localhost"      # Could use "127.0.0.1"  
        UDP_PORT = 8080           # Assigned port # to communicate  
        PACKET_SIZE = 2048        # Size of each packet to send (can be adjusted)  
        SLEEP_TIME = 1            # Intervals to prevent overloading  
  
a.	The setup for “clientUDP.py’s library and parameter is similar to “serverUDP.py”.  
b.	On “clientUDP.py”, first, two libraries are imported (socket and time). Socket is to allow for communications through the network, and time allows us to use intervals to prevent bottleneck. This is done using “import socket” and “import time”.  
c.	Next parameters are setup. First, using “localhost” allow us to get the machine’s local IP address, but using “127.0.0.1” would also work. Either one is used to assign the machine’s IP address to UDP_IP.   
d.	UDP_PORT is used to assign a port number to allow direct communication between the client and server.  
e.	PACKET_SIZE is used to determine how many bits will each packet contain. The size can be changed to the user preference, but the larger the packet size the slower the transfer speed will be.  
f.	SLEEP_TIME is used as a 1 second interval to prevent bottleneck on the server while transferring the packets.  
  
5.	clientUDP.py Socket Setup:  
  
        # Create a UDP socket for the client  
        Clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

        # Uses timeout function from time library to prevent overload  
        Clientsock.settimeout(SLEEP_TIME)  

        # Connect to the server  
        server_address = (UDP_IP, UDP_PORT)  
        Clientsock.connect(server_address)  
  
a.	“Clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)”uses the socket function to create a UDP socket for the client, allowing it to communicate with others.  
b.	“Clientsock.settimeout(SLEEP_TIME)” sets up the 1 second interval between each packet transfer.  
c.	“server_address  = (UDP_IP, UDP_PORT)” and “Clientsock.connect(server_address)” are used to connect the client to the server.  
  
# 6.	clientUDP.py Image Transfer:  
  
    # Open the image file for reading  
    # Replace "bubbles.jpg" for another file image if desired.  
    with open("bubbles.jpg", "rb") as image_file:  
        # Read the file in Packets  
        Packet = image_file.read(PACKET_SIZE)  

        while Packet:  
            # Send the Packet to the server  
            sent = Clientsock.send(Packet)  

            # Wait for the next Packet  
            print("A chunk of the image was sent as a packet ")  
            time.sleep(SLEEP_TIME)  

            # Read the next Packet from the file  
            Packet = image_file.read(PACKET_SIZE)  
  
    print("image was sent")  # Validate the send operation on screen  
    # Close the socket when complete  
    Clientsock.close()  
  
a.	Using “with open("bubbles.jpg", "rb") as image_file:” opens up the image file “bubbles.jpg” from the same local folder as “clientUDP.py”. using the command “rb” (read bits), will allows us to break down the image into bits.  
b.	“Packet = image_file.read(PACKET_SIZE)” set the bits into packets.  
c.	The while loop “While Packet:” will continuously send the packets to the server using “sent = Clientsock.send(Packet)”. Meanwhile, a print statement will tell the user whenever a packet is sent to the server.  
d.	“time.sleep(SLEEP_TIME)” will make use of the 1 second interval to prevent bottleneck.  
e.	Then, the next set of bits from the image is sent to “Packet” using “Packet = image_file.read(PACKET_SIZE)” again and, it will cycle till all the bits from the image is sent.  
f.	When the image has been completely sent, a print state will notify the user that it has been complete.  
g.	Lastly, the client’s socket is closed using “Clientsock.close()”.  
  
# Execution Example:  
