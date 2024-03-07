# ChatBackend.py
import socket
import threading
import datetime
from config import IP_ADDRESS, PORT

class ChatBackend:
    def __init__(self, gui, username):
        # Socket connection
        self.client_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        # Reference to the GUI for updating the textbox
        self.gui = gui

        # Start threads for sending and receiving messages
        self.receive_thread = threading.Thread(
            target=self.receive_messages
        )

        self.username = username
        # No default port
        self.port = None

    def connect(self, port):
        # Disconnect from the current port if connected
        if self.port is not None:
            self.client_socket.close()
            self.client_socket = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

        self.port = port
        self.client_socket.connect((IP_ADDRESS, self.port))
        
        # Create a new receive_thread and start it
        self.receive_thread = threading.Thread(
            target=self.receive_messages
        )
        self.receive_thread.start()


    def send_message(self, message):
        # Add the username, current time, and message
        message_with_username_and_time = (
            f"{self.username} "
            f"[{datetime.datetime.now().strftime('%X')}] "
            f": \n{message}"
        )
        self.client_socket.send(
            message_with_username_and_time.encode('utf-8')
        )
        # Insert the sent message into the textbox
        self.gui.textbox.insert(
            'end',
            message_with_username_and_time + '\n'
        )

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                self.gui.textbox.insert(
                    'end',
                    data.decode('utf-8') + '\n'
                )
            except Exception as e:
                print(f"Erreur de réception: {str(e)}")
                break

