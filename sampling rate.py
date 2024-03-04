import soundfile as sf

def get_sampling_rate(audio_path):
    audio_data, sr = sf.read(audio_path)
    return sr

# Path to the filtered audio
filtered_audio_path = r'C:\Users\Archit Singla\Downloads\filtered_breathing.wav'
new_sr = get_sampling_rate(filtered_audio_path)
print("Sampling rate of filtered audio:", new_sr)
