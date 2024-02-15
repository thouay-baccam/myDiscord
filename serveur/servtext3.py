import socket
import threading
import signal
import sys
import mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import MySQLConnectionPool
from datetime import datetime
from serveur.pc import DB_CONFIG, SERVER_CONFIG

# Utilisez DB_CONFIG et SERVER_CONFIG au lieu des valeurs directes
SERVER_IP = SERVER_CONFIG["ip"]
SERVER_PORT = SERVER_CONFIG["port"]

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à l'adresse et au port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Écoute pour les connexions entrantes
server_socket.listen()

print(f"Le serveur écoute sur {SERVER_IP}:{SERVER_PORT}")

# Connexion à la base de données MySQL avec pool
db_connection_pool = MySQLConnectionPool(pool_name="db_pool", pool_size=10, **DB_CONFIG)

# Liste pour stocker les clients connectés
clients = []
server_running = True  # Variable pour contrôler l'état du serveur

# Fonction pour envoyer les anciens messages au nouveau client
def send_old_messages(client_socket):
    try:
        connection = db_connection_pool.get_connection()
        cursor = connection.cursor()
        query = "SELECT content, sender, timestamp FROM messages_svc3 ORDER BY timestamp ASC"
        cursor.execute(query)
        old_messages = cursor.fetchall()
        cursor.close()
        connection.close()

        for old_message in old_messages:
            content, sender, timestamp = old_message
            message = f"{timestamp} - {sender}: {content}\n"
            client_socket.send(message.encode('utf-8'))

    except Error as e:
        print(f"Erreur lors de la récupération des anciens messages: {e}")

# Fonction pour gérer les messages entrants de chaque client
def handle_client(client_socket, client_address):
    try:
        # Envoyer les anciens messages au nouveau client lors de la connexion
        send_old_messages(client_socket)

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = f"{client_address[0]}:{client_address[1]} - {data.decode('utf-8')}"
            print(message)

            # Sauvegarder le message dans la base de données
            save_message_to_database(data.decode('utf-8'), f"{client_address[0]}:{client_address[1]}")

            # Diffuser le message à tous les clients
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

# Fonction pour sauvegarder le message dans la base de données
def save_message_to_database(content, sender):
    try:
        connection = db_connection_pool.get_connection()
        cursor = connection.cursor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO messages (content, sender, timestamp) VALUES (%s, %s, %s)"
        cursor.execute(query, (content, sender, timestamp))
        connection.commit()
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Erreur lors de l'insertion du message dans la base de données: {e}")

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
