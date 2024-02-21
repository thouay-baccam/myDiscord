import socket
import pyaudio
import wave
from pynput import keyboard

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5  # Durée de l'enregistrement

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('SENSITIVE_DATA', 1012))

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Appuyez sur la touche 'r' pour commencer l'enregistrement vocal.")

frames = []
recording = False

def on_press(key):
    global recording
    if key == keyboard.Key.esc:
        return False
    elif key.char == 'r':
        if not recording:
            print("Enregistrement audio en cours...")
            recording = True

def on_release(key):
    global recording
    if key.char == 'r':
        print("Enregistrement terminé.")
        recording = False

# Collecte les presses et les releases des touches 'r'
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        if recording:
            data = stream.read(CHUNK)
            frames.append(data)

            # Si vous voulez arrêter l'enregistrement avec une autre touche, ajoutez une condition ici

            # Envoyez les données audio au serveur
            client_socket.sendall(data)
