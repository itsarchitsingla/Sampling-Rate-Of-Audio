
# Finding Sampling Rate

This project helps to find sampling rate of an audio. I did it with my breathing sample. 



## Roadmap

- First, Record the sample using a microphone.

- Then copy the path of the sample and paste it in the code (filtering_frequency.py) to filter out higher frequency.

- Your filtered file will be saved in the folder.

- Then copy its path and paste it in breathing_sample.py, and then it will print the sampling rate.


## Sampling Rate

![App Screenshot](https://i.postimg.cc/VvLtGFy4/sampling-rate.png)

# Filtering Frequency Code

```python
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
```


## Sampling Rate Code

```python
import soundfile as sf

def get_sampling_rate(audio_path):
    audio_data, sr = sf.read(audio_path)
    return sr

# Path to the filtered audio
filtered_audio_path = r'C:\Users\Archit Singla\Downloads\filtered_breathing.wav'
new_sr = get_sampling_rate(filtered_audio_path)
print("Sampling rate of filtered audio:", new_sr)
```



