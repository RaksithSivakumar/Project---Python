import pvporcupine
import pyaudio

# Replace this with your actual access key
access_key = "d1UCYFKb2efm6HKQnE5Z9ULT9kClgLhzwAcU0CpcdX4iUvEqwtflHg=="

# Initialize Porcupine with the access key and the desired keyword
porcupine = pvporcupine.create(
    access_key=access_key,
    keywords=["picovoice"]  # Replace with your desired keyword(s)
)

# Setup PyAudio
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=porcupine.sample_rate,
                 input=True,
                 frames_per_buffer=porcupine.frame_length)

print("Listening for wake word...")

try:
    while True:
        pcm = stream.read(porcupine.frame_length)
        pcm = [int.from_bytes(pcm[i:i+2], byteorder='little', signed=True) for i in range(0, len(pcm), 2)]

        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("Hotword detected!")
except KeyboardInterrupt:
    print("\nStopping the hotword detection...")
finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
    porcupine.delete()
