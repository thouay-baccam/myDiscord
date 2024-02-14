import socket
import threading

clients = []  # Liste pour stocker les connexions des clients

def handle_client(client_socket, address):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            broadcast(message, address)
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        remove_client(client_socket, address)

def broadcast(message, sender_address):
    for client_socket, client_address in clients:
        if client_address != sender_address:
            try:
                client_socket.send(message.encode())
            except Exception as e:
                print(f"Error broadcasting message to {client_address}: {e}")

def remove_client(client_socket, address):
    try:
        print(f"Client {address} disconnected")
        clients.remove((client_socket, address))
        client_socket.close()
        broadcast(f"User {address} left the chat", address)
    except Exception as e:
        print(f"Error removing client {address}: {e}")

def start_server():
    server_ip = "0.0.0.0"  # Accept connections from any IP
    server_port = 34567

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Server listening on {server_ip}:{server_port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            clients.append((client_socket, client_address))
            broadcast(f"User {client_address} joined the chat", client_address)

            # Create a new thread to handle the client
            threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True).start()
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()

