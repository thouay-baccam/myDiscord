import socket
import base64
import pyaudio

# Configuration du client
SERVER_IP = 'SENSITIVE_DATA'
SERVER_PORT = 1012

# Configuration audio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialisation du client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Appuyez sur la touche 'r' pour commencer l'enregistrement vocal.")

frames = []
recording = False

while True:
    user_input = input("Entrez 'r' pour commencer l'enregistrement vocal, 's' pour arrêter, 'q' pour quitter: ")

    if user_input == 'r':
        if not recording:
            print("Enregistrement audio en cours...")
            recording = True
    elif user_input == 's':
        if recording:
            print("Enregistrement terminé.")
            recording = False

            # Arrêtez l'enregistrement et obtenez les frames
            stream.stop_stream()
            stream.close()
            audio.terminate()

            # Convertir les frames en un seul flux d'octets
            audio_data = b''.join(frames)

            # Envoyer les données audio au serveur
            client_socket.sendall(audio_data)

            # Reprenez l'enregistrement
            audio = pyaudio.PyAudio()
            stream = audio.open(format=FORMAT, channels=CHANNELS,
                                rate=RATE, input=True,
                                frames_per_buffer=CHUNK)
            frames = []
    elif user_input == 'q':
        break
