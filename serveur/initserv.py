import socket

# Créez un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lie le socket à une adresse et un port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Écoute les connexions entrantes (avec une limite de 5 connexion en attente)
server_socket.listen(5)

print('Le serveur écoute sur {}:{}'.format(*server_address))

# ATTEND la connection du client
client_socket, client_address = server_socket.accept()
