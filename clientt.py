import socket
import crcmod
import random

# Set the IP address and port number for the server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8888

# Set the maximum buffer size for receiving data
BUFFER_SIZE = 4096

# Set the maximum payload size for each packet
MAX_PAYLOAD_SIZE = 1000

import random

def corrupt_32_bit(data, probability=0.01):
    """
    Corrupts a data chunk by flipping a random bit with a given probability.

    :param data: The data chunk to corrupt.
    :param probability: The probability of flipping a bit (default is 0.01).
    :return: The corrupted data chunk.
    """
    # Split the data into 32-bit chunks
    chunks = [data[i:i+4] for i in range(0, len(data), 4)]

    # Corrupt each chunk with the given probability
    for i in range(len(chunks)):
        int_value = int.from_bytes(chunks[i], byteorder='big')
        byte_value = chunks[i]
        bit_to_flip = random.randint(0, 31)
        if random.random() < probability:
            byte_value = bytearray(byte_value)
            byte_value[3 - bit_to_flip // 8] ^= (1 << (bit_to_flip % 8))
            int_value = int.from_bytes(bytes(byte_value), byteorder='big')
        chunks[i] = int_value.to_bytes(4, byteorder='big')

    # Join the chunks back into a single data chunk
    return b''.join(chunks)



# Create a UDP socket for sending data
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set up the CRC-32 checksum generator
crc32_func = crcmod.mkCrcFun(0x104c11db7, 0, True, 0)

# Open the file to be sent
FILE_NAME = 'AWS.jpg'
with open(FILE_NAME, 'rb') as f:
    # Initialize the sequence number to 0
    seq_num = 0
    
    while True:
        # Read the next chunk of data from the file
        data_chunk = f.read(MAX_PAYLOAD_SIZE)
        
        # If the end of the file has been reached, send an empty packet to signify the end of the file transfer and break out of the loop
        if not data_chunk:
            client_socket.sendto(b'', (SERVER_IP, SERVER_PORT))
            print('End of file transfer')
            break

        data_chunk = corrupt_32_bit(data_chunk)

        # Calculate the CRC-32 checksum for the data chunk
        checksum = crc32_func(seq_num.to_bytes(4, byteorder='big') + data_chunk)
        
        # Construct the packet to be sent, including the sequence number, data chunk, and checksum
        packet = seq_num.to_bytes(4, byteorder='big') + data_chunk + checksum.to_bytes(4, byteorder='big')
        
        # Send the packet to the server
        client_socket.sendto(packet, (SERVER_IP, SERVER_PORT))
        print('Packet', seq_num, 'sent')
        
        # Wait for an acknowledgment from the server
        while True:
            ack_packet, server_addr = client_socket.recvfrom(BUFFER_SIZE)
            ack_seq_num = int.from_bytes(ack_packet[:4], byteorder='big')
            
            # If the acknowledgment sequence number matches the current sequence number, break out of the loop and move on to the next packet
            if ack_seq_num == seq_num:
                print('Acknowledgment', seq_num, 'received')
                seq_num += 1
                break

# Close the socket
client_socket.close()
