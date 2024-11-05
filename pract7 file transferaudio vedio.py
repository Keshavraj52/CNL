######TEXT/AUDIO/VIDEO#######

#############################SERVER.PY#############################
import socket

# Server IP address and port
HOST = '127.0.0.1'
PORT = 12345       

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address
s.bind((HOST, PORT))
print("Server is listening...")

BUFFER_SIZE = 65535  # Maximum size for a UDP packet

# Define a mapping of file types to proper extensions
file_type_mapping = {
    'audio': 'mp3',     # For audio files
    'video': 'mp4',     # For video files
    'text': 'txt',      # For text files
}

while True:
    print("Waiting for a new file...")

    # Receive file type or exit command
    file_type, addr = s.recvfrom(BUFFER_SIZE)
    file_type = file_type.decode().strip()  # Decode and clean the received file type

    # Check if the client sent the "exit" command
    if file_type.lower() == "exit":
        print("Exit command received. Shutting down the server.")
        break  # Exit the loop to close the server

    # Get the correct extension from the mapping or default to 'bin' if unknown
    file_extension = file_type_mapping.get(file_type, 'bin')
    file_name = f"received_file.{file_extension}"  # Save the file with the appropriate extension

    print(f"Receiving a {file_type} file from {addr}...")

    # Open the file to write binary data
    with open(file_name, 'wb') as f:
        while True:
            data, addr = s.recvfrom(BUFFER_SIZE)  # Receive file data
            if data == b'EOF':  # End of file indicator
                print(f"File has been received and saved as '{file_name}'.")
                break  # Break when the entire file is received
            f.write(data)  # Write the received data to the file

# Close the socket after the exit command
s.close()
print("Server has been closed.")



#############################CLIENT.PY#############################

import socket
import os

# Server IP address and port
HOST = '127.0.0.1'
PORT = 12345       

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# File paths for text, audio, and video
file_paths = {
    'text': r'text_path',
    'audio': r'audio_path',
    'video': r'video_path'
}

while True:
    try:
        # Prompt user to choose the file type
        file_type = input("Enter the type of file to send (text/audio/video or 'exit' to quit): ").lower()

        if file_type == 'exit':
            # Send the exit command to the server
            s.sendto(b'exit', (HOST, PORT))
            print("Exiting client.")
            break

        # Check if the file type is valid
        if file_type in file_paths:
            file_path = file_paths[file_type]

            # Check if the file exists
            if os.path.exists(file_path):
                # Send file type to the server first
                s.sendto(file_type.encode(), (HOST, PORT))

                # Send file data in chunks
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(128)  # Read data in chunks of 128 bytes
                        if not data:
                            break  # Stop reading when no more data
                        s.sendto(data, (HOST, PORT))  # Send the data

                # Send 'EOF' to indicate the end of file
                s.sendto(b'EOF', (HOST, PORT))
                print(f"{file_type.capitalize()} file has been sent successfully.")
            else:
                print("File not found. Please check the file path.")
        else:
            print("Invalid file type entered.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Close the socket once the loop ends
s.close()

