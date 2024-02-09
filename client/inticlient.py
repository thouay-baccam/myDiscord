from threading import Thread
import socket
import datetime

def send(sock, username):
    while True:
        message = input()
        if message.lower() == 'exit':
            sock.close()
            break
        formatted_message = f"{datetime.datetime.now().strftime('%H:%M:%S')} {username}: {message}"
        sock.send(formatted_message.encode('utf-8'))

def receive(sock):
    while True:
        try:
            response = sock.recv(500)
            if not response:
                break
            print(response.decode('utf-8'))
        except Exception as e:
            print(f"Erreur de réception : {e}")
            break

host = "SENSITIVE_DATA"
port = 1212

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

username = input("Entrez votre nom d'utilisateur : ")
client_socket.send(username.encode('utf-8'))

send_thread = Thread(target=send, args=(client_socket, username))
receive_thread = Thread(target=receive, args=(client_socket,))

send_thread.start()
receive_thread.start()

# Attendez que les threads se terminent avant de fermer le socket
send_thread.join()
receive_thread.join()

client_socket.close()
