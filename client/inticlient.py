import socket
import threading

# Adresse IP et port du serveur
SERVER_IP = 'SENSITIVE_DATA'
SERVER_PORT = 1212

# Création du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((SERVER_IP, SERVER_PORT))

# Fonction pour envoyer les messages au serveur
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Fonction pour recevoir les messages du serveur
def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        except Exception as e:
            print(f"Erreur de réception: {str(e)}")
            break

# Démarrer deux threads pour envoyer et recevoir des messages simultanément
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_messages)

send_thread.start()
receive_thread.start()
