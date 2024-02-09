import socket
import threading
import signal
import sys

# Adresse IP et port du serveur
SERVER_IP = '0.0.0.0'  # Accepte toutes les adresses IP
SERVER_PORT = 1212

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à l'adresse et au port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Écoute pour les connexions entrantes
server_socket.listen()

print(f"Le serveur écoute sur {SERVER_IP}:{SERVER_PORT}")

# Liste pour stocker les clients connectés
clients = []
server_running = True  # Variable pour contrôler l'état du serveur

# Fonction pour gérer les messages entrants de chaque client
def handle_client(client_socket, client_address):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = f"{client_address[0]}:{client_address[1]} - {data.decode('utf-8')}"
            print(message)
            broadcast(message, client_socket)

    except Exception as e:
        print(f"Erreur de connexion avec {client_address}: {str(e)}")
    finally:
        clients.remove(client_socket)
        client_socket.close()


# Fonction pour diffuser un message à tous les clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Erreur d'envoi au client: {str(e)}")


# Fonction pour arrêter proprement le serveur
def stop_server(signum, frame):
    global server_running
    print("Arrêt du serveur...")
    server_running = False
    server_socket.close()
    sys.exit(0)


# Associer la fonction stop_server au signal SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, stop_server)

# Boucle principale pour accepter les connexions des clients
while server_running:
    try:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

    except Exception as e:
        if server_running:
            print(f"Erreur lors de l'acceptation de la connexion: {str(e)}")

# Si la boucle principale se termine, cela signifie que le serveur a été arrêté
print("Serveur arrêté.")
