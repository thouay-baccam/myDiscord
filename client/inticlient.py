import socket
import threading
from datetime import datetime
from clientconfig import CLIENT_CONFIG


def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
    except Exception as e:
        print(f"Error receiving message: {e}")
    finally:
        client_socket.close()

def send_messages(client_socket):
    try:
        while True:
            user_input = input()
            formatted_message = f"[{datetime.now().strftime('%H:%M:%S')}] {user_input}"
            client_socket.send(formatted_message.encode())
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        client_socket.close()

def start_client():
    server_ip = CLIENT_CONFIG["server_ip"]
    server_port = CLIENT_CONFIG["server_port"]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    send_thread = threading.Thread(target=send_messages, args=(client_socket,), daemon=True)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

if __name__ == "__main__":
    start_client()
