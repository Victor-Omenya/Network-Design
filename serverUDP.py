# Import socket and time library
import socket
import time

# Configuration parameters for server
UDP_IP = "localhost"    # Could use "127.0.0.1"
UDP_PORT = 8080         # Assigned port # to communicate
PACKET_SIZE = 2048      # Size of each packet to send (can be adjusted)
SLEEP_TIME = 1          # Intervals to prevent overloading

# Create a UDP socket for the server
Serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = (UDP_IP, UDP_PORT)
Serversock.bind(server_address)

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
    
        
