######UDP#######

#############################SERVER.PY#############################

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Successfully created")
port=3528
host=socket.gethostbyname('localhost')

s.bind((host,port))
print("Socket binded to %s"%(port))

s.listen(5)
print("Socket is listening")

while True:
    c, addr=s.accept()
    print("Got connection from ",addr)
    c.send("Thank you for connecting".encode())
    c.close()
    break

#############################CLIENT.PY#############################

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=3528
host=socket.gethostbyname('localhost')
s.connect((host,port))
print(s.recv(1024).decode())
s.close()


####TCP####

############################SERVER.PY#############################

import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
localip='127.0.0.1'
localport=30945
buffersize=1024
message="Message for UDP client from UDP server"
encode=message.encode()

sock.bind((localip,localport))
print("UDP server up and listening")
while(True):
    bytesAddressPair = sock.recvfrom(buffersize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client: {}".format(message.decode())
    clientIP = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    sock.sendto(encode, address)


############################CLIENT.PY########################

import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msgFromClient = "Message for UDP server from UDP client"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 30945)
bufferSize = 1024
sock.sendto(bytesToSend, serverAddressPort)

msgFromServer = sock.recvfrom(bufferSize)
msg = "Message from Server: {}".format(msgFromServer[0].decode())
print(msg)

