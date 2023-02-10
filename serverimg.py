import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('127.0.0.1', 1200)
server_socket.bind(server_address)

print("Server is ready to receive image data.")

# Receive data from the client
while True:
    data, client_address = server_socket.recvfrom(4096)
    
    # Write the received data to a file
    with open('received_image.jpg', 'wb') as f:
        f.write(data)
    
    print("Image file has been received successfully.")
    break

# Close the socket
server_socket.close()