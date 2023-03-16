import socket

# Configuration parameters for client
UDP_IP = 'localhost'      # Could use "127.0.0.1"
UDP_PORT = 8080           # Assigned port # to communicate
PACKET_SIZE = 2048        # Size of each packet to send (can be adjusted)
SLEEP_TIME = 1            # Intervals to prevent overloading

def calculate_checksum(data):
    checksum = 0
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            checksum += (data[i] << 8) + data[i+1]
        else:
            checksum += data[i]
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    return (~checksum & 0xFFFF)

# Create a UDP socket for the client
Clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Uses timeout function from time library to prevent overload
Clientsock.settimeout(SLEEP_TIME)

# Connect to the server
server_address = (UDP_IP, UDP_PORT)
# Open the image file for reading
# Replace "bubbles.jpg" for another file image if desired.
with open("AWS.jpg", "rb") as f:
    image_data = f.read(PACKET_SIZE)
    
    # Initialize sequence number
    seq_num = 0

    # Send packets with sequence numbers
    while image_data:
        checksum = calculate_checksum(image_data)
        packet = f'{seq_num}:{checksum}:'.encode() + image_data
        Clientsock.sendto(packet, server_address)
        print(f'Sent packet {seq_num}')

        # Wait for ACK
        while True:
            try:
                ack, server_address = Clientsock.recvfrom(PACKET_SIZE)
                ack_num = int(ack.decode())
                if ack_num == seq_num:
                    print(f'Received ACK for packet {ack_num}')
                    seq_num = 1 - seq_num  # Flip sequence number
                    break
            except socket.timeout:
                print(f'Timeout. Resending packet {seq_num}')
                Clientsock.sendto(packet, server_address)

        # Read next packet
        image_data = f.read(PACKET_SIZE)

print("Image file has been sent successfully.")
