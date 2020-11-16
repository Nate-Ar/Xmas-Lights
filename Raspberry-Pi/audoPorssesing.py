import librosa, librosa.display
import matplotlib.pyplot as plt
import time
file = "test.wav"
signal, sr = librosa.load(file, sr=22050)
librosa.display.waveplot(signal, sr=sr)

y, sr = librosa.load(file)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print("{} beats pre sec".format(round(tempo/60, 1)))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
def song():
    while True:
        rounded = round(tempo/60, 1)
        print("beat")
