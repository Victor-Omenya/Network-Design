# Import socket library
import socket

# Configuration parameters for server
UDP_IP = 'localhost'   # Could use "127.0.0.1"
UDP_PORT = 1200        # Assigned port # to communicate
PACKET_SIZE = 1024     # Size of each packet to receive (can be adjusted)

def calculate_checksum(data):
    checksum1 = 0
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            checksum1 += (data[i] << 8) + data[i+1]
        else:
            checksum1 += data[i]
        checksum1 = (checksum1 & 0xFFFF) + (checksum1 >> 16)
    return (~checksum1 & 0xFFFF)

# Create a UDP socket for the server
serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
serversock.bind((UDP_IP, UDP_PORT))

# Open a file to write the image data to
# Replace "received_image.jpg" for another filename if desired
with open("received_image.jpg", "wb") as f:
    expected_seq_num = 0
    while True:
        # Receive the next packet
        packet, client_address = serversock.recvfrom(PACKET_SIZE)
        
        # Extract the sequence number and checksum from the packet
        packet_data = packet.decode().split(":")
        seq_num = int(packet_data[0])
        checksum = int(packet_data[1])
        data = packet_data[2].encode()
        
        # Validate the checksum
        if calculate_checksum(data) != checksum:
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
        
        # Send an ACK for the packet
        ack_packet = str(seq_num).encode()
        serversock.sendto(ack_packet, client_address)
        
        # If all packets have been received, break out of the loop
        if not packet:
            break

print("Image file has been received and written to disk.")
