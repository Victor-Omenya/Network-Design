import socket
import crcmod

# Set the IP address and port number for the server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8888

# Set the maximum buffer size for receiving data
BUFFER_SIZE = 4096

# Set the maximum payload size for each packet
MAX_PAYLOAD_SIZE = 1000

# Create a UDP socket for receiving data
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f'Server listening on {SERVER_IP}:{SERVER_PORT}...')

# Set up the CRC-32 checksum generator
crc32_func = crcmod.mkCrcFun(0x104c11db7, 0, True, 0)

# Initialize the expected sequence number to 0
expected_seq_num = 0

# Open the output file for writing
FILE_NAME = 'test_received.jpg'
with open(FILE_NAME, 'wb') as f:
    while True:
        # Receive a packet from the client
        packet, client_addr = server_socket.recvfrom(BUFFER_SIZE)
        seq_num = int.from_bytes(packet[:4], byteorder='big')
        data_chunk = packet[4:-4]
        checksum = int.from_bytes(packet[-4:], byteorder='big')
        
        # Calculate the CRC-32 checksum for the received data
        calculated_checksum = crc32_func(seq_num.to_bytes(4, byteorder='big') + data_chunk)
        
        # If the received checksum matches the calculated checksum and the sequence number is correct, write the data chunk to the output file and send an acknowledgment
        if checksum == calculated_checksum and seq_num == expected_seq_num:
            f.write(data_chunk)
            print('Packet', expected_seq_num, 'received')
            ack_packet = (expected_seq_num).to_bytes(4, byteorder='big') + (checksum).to_bytes(4, byteorder='big')
            server_socket.sendto(ack_packet, client_addr)
            print('Acknowledgment', expected_seq_num, 'sent')
            expected_seq_num += 1
        # If the received checksum does not match the calculated checksum or the sequence number is incorrect, send an acknowledgment with the previous sequence number
        else:
            print('Packet', seq_num, 'discarded')
            if expected_seq_num > 0:
                ack_packet = (expected_seq_num - 1).to_bytes(4, byteorder='big') + (checksum).to_bytes(4, byteorder='big')
                server_socket.sendto(ack_packet, client_addr)
                print('Acknowledgment', expected_seq_num - 1, 'sent')
