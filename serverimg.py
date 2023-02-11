import socket

# Configuration parameters
Host = "127.0.0.1"
Port = 12000
buff = 1024

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and Port
server_address = (Host, Port)
server_socket.bind(server_address)

print("The server is ready to receive the file")

# Open the image file for writing
with open("received_img.jpg", "wb") as image_file:
    try:
        while True:
        # Receive the chunk from the client
            data, address = server_socket.recvfrom(buff)

        # Write the chunk to the file
            image_file.write(data)

        # Send ACK to the client
            server_socket.sendto(b"ACK", address)
    except:
        server_socket.close()
        print("File Downloaded. Check the folder in the same path")
        
        
       

