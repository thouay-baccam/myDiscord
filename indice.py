import pyaudio

audio = pyaudio.PyAudio()

print("Liste des périphériques audio d'entrée disponibles:")
for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    print(f"Index {i}: {device_info['name']}")

audio.terminate()