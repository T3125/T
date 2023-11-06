import socket

udpser=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serv_addr=('127.0.0.1',1431)

udpser.bind(serv_addr)
print(f"UDP serve is listening on {serv_addr}")

while True:
    data,client=udpser.recvfrom(1024)
    print(f"Received msg form {client}:{data.decode('utf-8')}")

    response=b"hello hi"
    udpser.sendto(response,client)