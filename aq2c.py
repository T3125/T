import socket
client=socket.socket()
server_add=('127.0.0.1',1231)
client.connect(server_add)
print("connected to server")
fi=open("input.txt","r")
data=fi.read()
client.send(data.encode('utf-8'))
print("File sent Successfully")
fi.close()
client.close()
print("Connection Closed")