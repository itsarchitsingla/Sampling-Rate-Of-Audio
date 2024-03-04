import librosa
import numpy as np
import scipy.signal
from scipy.io.wavfile import write as write_wav

def remove_high_frequency(audio_path, cutoff_freq=500):
    # Load audio
    y, sr = librosa.load(audio_path, sr=None)
    
    # Designing low-pass filter
    nyquist = sr / 2.0
    cutoff = cutoff_freq / nyquist
    b, a = scipy.signal.butter(5, cutoff, btype='low')
    
    # Apply filter
    y_filtered = scipy.signal.filtfilt(b, a, y)
    
    return y_filtered, sr

# Path to your recorded breathing sound
audio_path = 'C:\\Users\\Archit Singla\\Downloads\\v5qk0-3upfe.mp3'
filtered_audio, sr = remove_high_frequency(audio_path)

# Save the filtered audio
write_wav('filtered_breathing.wav', sr, filtered_audio.astype(np.float32))
