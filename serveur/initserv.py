from threading import Thread
import socket

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                # En cas d'échec de l'envoi, retirez le client de la liste
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(500)
            if not message:
                break
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Erreur de réception : {e}")
            break

host = "0.0.0.0"
port = 1212

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print("Le serveur est en écoute sur", host, "et le port", port)

while True:
    client, address = server_socket.accept()
    clients.append(client)
    print(f"Le client d'IP {address} s'est connecté")

    client_handler = Thread(target=handle_client, args=(client,))
    client_handler.start()
