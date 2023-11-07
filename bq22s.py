import socket
import random
server_address = ('localhost', 4446)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)
window_size = 4
expected_sequence_number = 0
buffer={}
while True:
    data, client_address = server_socket.recvfrom(1024)
    packet_number = int(data.decode())
    if random.random() < 0.2:
        print(f"Received: {packet_number}, Acknowledgment not sent for packet {packet_number}")
    else:
        buffer[packet_number] = packet_number
        print(f"Sending ACK for {packet_number}")
        server_socket.sendto(str(packet_number).encode(),client_address)
        while expected_sequence_number in buffer:
            expected_sequence_number+=1
server_socket.close()
