import socket
import random
server_address=('127.0.0.1',1234)
receiver_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
receiver_socket.bind(server_address)
while True:
    data,client_address=receiver_socket.recvfrom(1024)
    packet=data.decode()
    packet_number=int(packet.split()[1])
    if random.random()<0.2:
        print(f"Received:{packet}, Acknowledgement not sent fro packet {packet_number}")
    else:
        receiver_socket.sendto(str(packet_number).encode(),client_address)
        print(f"Recived:{packet},sent ACK: {packet_number}")
reciver_socket.close()
