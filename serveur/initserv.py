from threading import Thread
import socket
import datetime

clients = []

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(500).decode('utf-8')
            if not message:
                break
            formatted_message = f"{datetime.datetime.now().strftime('%H:%M:%S')} {username}: {message}"
            broadcast(formatted_message, sender_socket=client_socket)
        except Exception as e:
            print(f"Erreur de réception : {e}")
            break

def broadcast(message, sender_socket=None):
    for client in clients:
        if client['socket'] != sender_socket:
            try:
                client['socket'].send(message.encode('utf-8'))
            except:
                # En cas d'échec de l'envoi, retirez le client de la liste
                clients.remove(client)

host = "0.0.0.0"
port = 1212

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print("Le serveur est en écoute sur", host, "et le port", port)

while True:
    client, address = server_socket.accept()
    username = client.recv(500).decode('utf-8')  # Attendre le nom d'utilisateur
    clients.append({'socket': client, 'username': username})
    print(f"Le client {username} d'IP {address} s'est connecté")

    client_handler = Thread(target=handle_client, args=(client, username))
    client_handler.start()
