import socket

# Create UDP client
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8080)

# Helper function to send a file
def send_file(filename):
    with open(filename, 'rb') as f:
        chunk = f.read(4096)
        while chunk:
            udp_client.sendto(chunk, server_address)
            chunk = f.read(4096)

    udp_client.sendto(b'EOF', server_address)
    print(f"File '{filename}' sent successfully.")

# Send video file
send_file('samplevideo.mp4')

# Send audio file
send_file('Soulmate.mp3')

# Send text file
send_file('document.txt')

# Send script file
send_file('sample_script.py')

udp_client.close()
