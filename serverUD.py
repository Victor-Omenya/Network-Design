# Import socket library
import socket

# Configuration parameters for server
UDP_IP = 'localhost'   # Could use "127.0.0.1"
UDP_PORT = 8080        # Assigned port # to communicate
PACKET_SIZE = 2048     # Size of each packet to receive (can be adjusted)

def calculate_checksum(packet):
    checksum = 0
    for i in range(0, len(packet), 2):
        if i + 1 < len(packet):
            w = (ord(packet[i]) << 8) + (ord(packet[i+1]))
            checksum += w
        else:
            w = (ord(packet[i]) << 8)
            checksum += w
    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum = checksum + (checksum >> 16)
    return (~checksum) & 0xffff

# Create a UDP socket for the server
serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
serversock.bind((UDP_IP, UDP_PORT))
print("server is ready to receive the image")

# Open a file to write the image data to
# Replace "received_image.jpg" for another filename if desired
with open("received_image.jpg", "wb") as f:
    expected_seq_num = 0
    received_data = b''

    while True:
        # Receive the next packet
        packet, client_address = serversock.recvfrom(PACKET_SIZE)
        
        # Extract the sequence number and checksum from the packet
        packet_data = packet.decode().split(":")
        seq_num = int(packet_data[0])
        checksum = int(packet_data[1])
        data = packet_data[2].encode()
        
        # Validate the checksum
        if int(calculate_checksum(data)) != checksum:
            print("Packet", seq_num, "has an invalid checksum. Resending ACK", expected_seq_num - 1)
            # Resend the ACK for the previous packet
            ack_packet = str(expected_seq_num - 1).encode()
            serversock.sendto(ack_packet, client_address)
            continue
        
        # If the packet has the expected sequence number, write the data to the file
        if seq_num == expected_seq_num:
            f.write(data)
            expected_seq_num += 1
            print("Packet", seq_num, "received and written to file.")
            received_data += data
        
        # Send an ACK for the packet
        ack_packet = str(seq_num).encode()
        serversock.sendto(ack_packet, client_address)
        
        # If all packets have been received, break out of the loop
        if not packet:
            break
with open("received_image.jpg", 'wb') as f:
    f.write(received_data)
print("Image file has been received and written to disk.")

