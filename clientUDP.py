import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 8080
PACKET_SIZE = 2048
SLEEP_TIME = 1

Clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Clientsock.settimeout(SLEEP_TIME)

# Connect to the server
server_address = (UDP_IP, UDP_PORT)
Clientsock.connect(server_address)

# Open the image file for reading
with open("bubbles.jpg", "rb") as image_file:
    
    # Read the file in Packets
    Packet = image_file.read(PACKET_SIZE)

    while Packet:
        # Send the Packet to the server
        sent = Clientsock.send(Packet)

        # Wait for the next Packet 
        print("A chunk of the image was sent as a packet")
        time.sleep(SLEEP_TIME)
        
        # Read the next Packet from the file
        Packet = image_file.read(PACKET_SIZE)
                
print("image was sent") #Validate the send operation on screen
# Close the socket
Clientsock.close()
