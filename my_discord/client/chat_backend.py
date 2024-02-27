# ChatBackend.py
import re
import socket
import threading
import datetime
from config import IP_ADDRESS, PORT

class ChatBackend:
    def __init__(self, gui, username):
        # Socket connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Reference to the GUI for updating the textbox
        self.gui = gui

        # Start threads for sending and receiving messages
        self.receive_thread = threading.Thread(target=self.receive_messages)

        self.username = username
        self.port = None  # No default port

    def connect(self, port):
        if self.port is not None:  # Disconnect from the current port if connected
            self.client_socket.close()
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.port = port
        self.client_socket.connect(('SENSITIVE_DATA', self.port))
        
        # Create a new receive_thread and start it
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def send_message(self, message):
        # Add the username, current time, and message
        message_with_username_and_time = f"{self.username} [{datetime.datetime.now().strftime('%H:%M:%S')}] : \n{message}"
        self.client_socket.send(message_with_username_and_time.encode('utf-8'))
        self.gui.chatbox_insert(message_with_username_and_time)

    def process_received_data(self, data):
        date_regex = r"(?:(?:[0-9]{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9]|3[01]))"
        processed_data = re.split(date_regex, data.decode('utf-8'))

        hour_regex = r"(?:(?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5][0-9]):(?:[0-5][0-9]))"
        start_match = re.match(hour_regex, processed_data[0])

        if not start_match and len(processed_data[0]) != 0:
            message_labels = self.gui.chatbox_frame.winfo_children()
            last_message_label = message_labels[-1].winfo_children()[0]

            current_text = last_message_label.cget("text")
            new_text = current_text + processed_data[0]

            last_message_label.configure(text = new_text)

            processed_data.pop(0)

        elif len(processed_data[0]) == 0:
            processed_data.pop(0)

        return processed_data

    # Find a way to reduce indentation
    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                for message in self.process_received_data(data):
                    if len(message) == 0:
                        continue
                    self.gui.chatbox_insert(message)
            except Exception as e:
                print(f"Erreur de réception: {str(e)}")
                break

