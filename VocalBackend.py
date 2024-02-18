import socket
import pyaudio
from conf import IP_ADDRESS, PORT

# Paramètres audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Initialisation du client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))

# Initialisation de l'objet PyAudio
audio_stream = pyaudio.PyAudio()
stream = audio_stream.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

try:
    while True:
        # Enregistrement audio depuis le microphone
        audio_data = stream.read(CHUNK)

        # Envoyer les données audio au serveur
        client_socket.sendall(audio_data)
except KeyboardInterrupt:
    print("Arrêt du client.")
finally:
    stream.stop_stream()
    stream.close()
    audio_stream.terminate()
    client_socket.close()
