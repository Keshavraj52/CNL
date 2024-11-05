import socket
import os
import subprocess
import time

# Time span (in seconds) to wait before opening the file
WAIT_TIME = 5

# Create UDP server
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('localhost', 8080))

print("UDP server listening for files...")

# Helper function to receive a file
def receive_file(filename):
    with open(filename, 'wb') as f:
        while True:
            data, client_address = udp_server.recvfrom(4096)
            if data == b'EOF':  # End of file marker
                break
            f.write(data)

    print(f"File '{filename}' received successfully.")
    
    # Automatically open the file after waiting
    print(f"Opening '{filename}' in {WAIT_TIME} seconds...")
    time.sleep(WAIT_TIME)
    
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(filename)
        elif os.name == 'posix':  # For macOS and Linux
            subprocess.run(['open', filename])  # For macOS
            # subprocess.run(['xdg-open', filename])  # For Linux
    except Exception as e:
        print(f"Error while trying to open the file: {e}")

# Receive video file
receive_file('received_video.mp4')

# Receive audio file
receive_file('received_audio.mp3')

# Receive text file
receive_file('received_text.txt')

# Receive script file
receive_file('received_script.py')

udp_server.close()
