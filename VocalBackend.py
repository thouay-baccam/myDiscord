import socket
import base64
import pyaudio
import threading
import keyboard

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('', ))

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

def on_press(key):
    if key == 'esc':
        stop_recording()
        client_socket.close()
        stream.stop_stream()
        stream.close()
        audio.terminate()
        return False
    elif key.char == 'r':
        start_recording()

def on_release(key):
    if key.char == 'r':
        stop_recording()

def start_recording():
    global recording, frames
    if not recording:
        print("Enregistrement audio en cours...")
        recording = True
        frames = []

def stop_recording():
    global recording, frames
    if recording:
        print("Enregistrement terminé.")
        recording = False
        audio_data = b''.join(frames)
        send_audio_data(audio_data)

def send_audio_data(audio_data):
    audio_text = base64.b64encode(audio_data).decode('utf-8')
    client_socket.sendall(audio_text.encode())

def receive_audio():
    while True:
        audio_text = client_socket.recv(1024).decode()
        if not audio_text:
            break
        play_audio(audio_text)

def play_audio(audio_text):
    audio_data = base64.b64decode(audio_text.encode())
    stream.write(audio_data)

recording = False
frames = []

# Créez un thread pour recevoir continuellement les messages audio du serveur
audio_thread = threading.Thread(target=receive_audio)
audio_thread.start()

# Configurez les gestionnaires d'événements pour le clavier
keyboard.on_press_key('r', on_press)
keyboard.on_release_key('r', on_release)
keyboard.wait('esc')  # Attendez que la touche 'esc' soit enfoncée pour terminer le programme

# Fermeture des ressources
client_socket.close()
stream.stop_stream()
stream.close()
audio.terminate()
