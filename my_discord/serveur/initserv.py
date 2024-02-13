import socket
import threading

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


# Fonction pour gérer les messages entrants de chaque client
def handle_client(client_socket, client_address):
    try:
        while True:
            # Recevoir les données du client
            data = client_socket.recv(1024)
            if not data:
                break

            # Diffuser le message à tous les clients
            message = f"{client_address[0]}:{client_address[1]} - {data.decode('utf-8')}"
            print(message)
            broadcast(message, client_socket)

    except Exception as e:
        print(f"Erreur de connexion avec {client_address}: {str(e)}")
    finally:
        # Retirer le client de la liste
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


# Boucle principale pour accepter les connexions des clients
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)

    # Démarrer un thread pour gérer le client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
