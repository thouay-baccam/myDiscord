import socket
import threading
import datetime
from config import IP_ADDRESS, PORT

class ChatBackend:
    def __init__(self, gui, username, db_connection):
        # Socket connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Reference to the GUI for updating the textbox
        self.gui = gui

        # Start threads for sending and receiving messages
        self.receive_thread = threading.Thread(target=self.receive_messages)

        self.username = username
        self.port = None  # No default port
        self.db_connection = db_connection

    def connect(self, port):
        if self.port is not None:  # Disconnect from the current port if connected
            self.client_socket.close()
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.port = port
        self.client_socket.connect((IP_ADDRESS, self.port))

        # Create a new receive_thread and start it
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

        # Update the user's status to online in the database
        query = "UPDATE users SET online=1 WHERE username=%s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (self.username,))
        self.db_connection.commit()

    def send_message(self, message):
        # Add the username, current time, and message
        message_with_username_and_time = f"{self.username} [{datetime.datetime.now().strftime('%H:%M:%S')}] : \n{message}"
        self.client_socket.send(message_with_username_and_time.encode('utf-8'))
        # Insert the sent message into the textbox
        self.gui.textbox.insert('end', message_with_username_and_time + '\n')

        # Update the notifications count in the database for all offline users
        query = "SELECT * FROM users WHERE online=0 AND username!=%s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (self.username,))
        offline_users = cursor.fetchall()

        for user in offline_users:
            query = "INSERT INTO notifications (username, message) VALUES (%s, %s)"
            cursor.execute(query, (user[1], message_with_username_and_time))
            self.db_connection.commit()

            # Update the user's notifications count
            query = "UPDATE users SET notifications=notifications+1 WHERE username=%s"
            cursor.execute(query, (user[1],))
            self.db_connection.commit()

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                self.gui.textbox.insert('end', data.decode('utf-8') + '\n')

                # Check if the message contains the user's username (mention)
                mention = f"@{self.username} "
                if data.decode('utf-8').startswith(mention):
                    # Play a sound or show a notification
                    pass
            except Exception as e:
                print(f"Erreur de réception: {str(e)}")
                break

        # Update the user's status to offline in the database
        query = "UPDATE users SET online=0 WHERE username=%s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (self.username,))
        self.db_connection.commit()
