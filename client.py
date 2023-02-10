import socket
import time

IP_ADDRESS = "127.0.0.1"
PORT = 1200
BUFFER_SIZE = 1024
TIMEOUT = 2

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.settimeout(TIMEOUT)

server_address = (IP_ADDRESS, PORT)
client_socket.connect(server_address)

with open("Test_IMG.jpg", "rb") as image_file:
    # Read the file in chunks
    chunk = image_file.read(BUFFER_SIZE)
    while chunk:
        # Send the chunk to the server
        sent = client_socket.send(chunk)

        # Wait for ACK from the server
        ack = False
        while not ack:
            try:
                # Receive the ACK from the server
                data, address = client_socket.recvfrom(BUFFER_SIZE)

                # Check if the ACK is valid
                if data == b"ACK":
                    ack = True
            except socket.timeout:
                # Resend the chunk if ACK is not received in time
                sent = client_socket.send(chunk)

        # Read the next chunk from the file
        chunk = image_file.read(BUFFER_SIZE)

# Close the socket
client_socket.close()
        
