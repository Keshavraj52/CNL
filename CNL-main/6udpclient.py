import socket

# Define server address and port
host = "127.0.0.1"
port = 12000
buffer_size = 1024
file_name = 'Myfile.txt'  # File to be sent to the server

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open the file and send its content
with open(file_name, 'r') as f:
    data = f.read(buffer_size)
    while data:
        sock.sendto(data.encode(), (host, port))  # Send file data in chunks
        data = f.read(buffer_size)

# Send end signal to the server
sock.sendto("Now".encode(), (host, port))

print("File successfully sent!")
sock.close()
