import socket
import time

# Configuration parameters
UDP_IP = "127.0.0.1"
UDP_PORT = 8080
PACKET_SIZE = 2048
SLEEP_TIME = 1

# Create a UDP socket
Serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = (UDP_IP, UDP_PORT)
Serversock.bind(server_address)

print("Server is ready to receive the image")

# Open the image file for writing
with open("received_image.jpg", "wb") as image_file:
    while True:
        # Receive data from the client
        data, client_address = Serversock.recvfrom(PACKET_SIZE)

        # Write the received data to the image file
        received_image = image_file.write(data)
        print("A chunk of the image was received as a packet")

        # Wait for the next Packet of data
        time.sleep(SLEEP_TIME)
    
        
