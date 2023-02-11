import socket

Host = "127.0.0.1"
Port = 12000
buff = 1024
TIMEOUT = 2

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.settimeout(TIMEOUT)

server_address = (Host, Port)
client_socket.connect(server_address)

with open("Test_IMG.jpg", "rb") as image_file:
    # Read the file in packets
    packet = image_file.read(buff)
    while packet:
        # Send the packet to the server
        sent = client_socket.send(packet)

        # Wait for ACK from the server
        ack = False
        while not ack:
            try:
                # Receive the ACK from the server
                data, address = client_socket.recvfrom(buff)

                # Check if the ACK is valid
                if data == b"ACK":
                    ack = True
            except socket.timeout:
                # Resend the packet if ACK is not received in time
                sent = client_socket.send(packet)

        # Read the next packet from the file
        packet = image_file.read(buff)

print("image was sent and acknowledgement was received")
# Close the socket
client_socket.close()
        
