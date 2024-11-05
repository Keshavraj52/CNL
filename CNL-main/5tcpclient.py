import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Connect to the server
s.connect((host, port))

# Receive data from the server
tm = s.recv(1024)
s.close()

# Print the received time from the server
print(f"The time got from the server is {tm.decode('ascii')}")
