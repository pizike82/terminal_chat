# Client Side Chat Room

import socket, threading, time

# Define Constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Create a cleint socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def send_message():
    # Send message to server to be broadcast
    while True:
        message = input("> ")
        client_socket.send(message.encode(ENCODER))


def recieve_message():
    # Recieve message from server
    while True:
        try:
            # Get incoming message
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            # Check for the NAME flag
            if message == "NAME":
                name = input("What is your name: ")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            # An error occured, close connection
            print("An error occured...")
            client_socket.close()
            break


# Create Threads
recieve_thread = threading.Thread(target=recieve_message)
send_thread = threading.Thread(target=send_message)

# Start the client
recieve_thread.start()
time.sleep(3)
send_thread.start()
