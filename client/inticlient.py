from threading import Thread
import socket

def send(sock):
    while True:
        msg = input()
        msg = msg.encode('utf-8')
        sock.send(msg)

def receive(sock):
    while True:
        try:
            response = sock.recv(500)
            response = response.decode("utf-8")
            print(response)
        except Exception as e:
            print(f"Erreur de réception : {e}")
            break

host = "86.71.172.58"
port = 1212  # Port externe configuré sur le routeur

# Création du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

send_thread = Thread(target=send, args=[client_socket])
receive_thread = Thread(target=receive, args=[client_socket])

send_thread.start()
receive_thread.start()

# Attendez que les deux threads se terminent avant de fermer le socket
send_thread.join()
receive_thread.join()

client_socket.close()
