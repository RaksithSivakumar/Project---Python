import sounddevice as sd
from scipy.io.wavfile import write

# Define recording parameters
sample_rate = 44100  # Samples per second
duration = 10   # Duration in second
output_file = "output.wav"  

print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
sd.wait()  
print("Recording finished.")

write(output_file, sample_rate, audio_data)
print(f"Audio saved as {output_file}")
