from threading import Thread
import socket

def send(client):
    while True:
        msg = input()
        msg = msg.encode("utf-8")
        client.send(msg)

def receive(client):
    while True:
        try:
            requete_client = client.recv(500)
            requete_client = requete_client.decode('utf-8')
            print(requete_client)
            if not requete_client:  # Si on perd la connexion
                print("CLOSE")
                break
        except Exception as e:
            print(f"Erreur de réception : {e}")
            break

def handle_client(client, address):
    print(f"Le client d'IP {address} s'est connecté")

    send_thread = Thread(target=send, args=[client])
    receive_thread = Thread(target=receive, args=[client])

    send_thread.start()
    receive_thread.start()

    receive_thread.join()

    client.close()
    print(f"Le client d'IP {address} s'est déconnecté")

# Paramètres du serveur
host = "SENSITIVE_DATA:1212"
port = 12345

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen(5)

print("Le serveur est en écoute sur", host, "et le port", port)

while True:
    client, address = server_socket.accept()
    client_handler = Thread(target=handle_client, args=(client, address))
    client_handler.start()
