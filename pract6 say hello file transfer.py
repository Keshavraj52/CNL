######SAY HELLO#######

#############################SERVER.PY#############################

import socket

HOST = '127.0.0.1' 
PORT = 3333  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept() 
    with conn:  
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()  
            print('Client says:', data)

            if data == 'stop':  
                print("Stopping the server...")
                break

            str2 = input("Enter your message: ") 
            conn.sendall(str2.encode()) 

#############################CLIENT.PY#############################

import socket

HOST = '127.0.0.1'  
PORT = 3333  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    while True:
        message = input("Enter your message: ")  # Get user input
        s.sendall(message.encode())  # Send the message to the server

        if message == 'stop':  # Break if 'stop' message is sent
            print("Stopping the client...")
            break

        data = s.recv(1024).decode()  # Receive data from the server
        print('Server says:', data)  # Print the server's response



####FILE_TRANSFER####

############################SERVER.PY#############################

import socket

host = "127.0.0.1"
port = 12000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))  

with open('Myfile2.txt', 'wb') as f:  
    print('New file created')
    data, addr = sock.recvfrom(1024)

    while data:
        print(data)
        if data.decode("utf-8") == "Now":
            break
        f.write(data)  
        data, addr = sock.recvfrom(1024) 

    print('File is successfully received!!!')


with open('Myfile2.txt', 'r') as f:
    print(f.read()) 

sock.close() 
print('Connection closed!')



############################CLIENT.PY########################

import socket

host = "127.0.0.1"
port = 12000
buffer_size = 1024
file_name = r'file_path'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

with open(file_name, "r") as f:  

    data = f.read(buffer_size)
    while data:
        print(data) 
        sock.sendto(data.encode(), (host, port)) 
        data = f.read(buffer_size)  

    sock.sendto("Now".encode(), (host, port))

sock.close()  # Close the socket



