import socket

# Créez un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection au serveur
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Envoye des données
message = "Hello, server!"
client_socket.sendall(message.encode())

# Attend une réponse
data = client_socket.recv(1024)
print('Received:', data.decode())

# pour fermer la connexion
client_socket.close()
