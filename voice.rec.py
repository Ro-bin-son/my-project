import sounddevice as sd, scipy.io.wavfile as wav

sec = int(input("Record seconds: "))
audio = sd.rec(sec * fs, samplerate=fs, channels=2)
sd.wait()

wav.write("record.wav",fs, audio)
print("Saved record.wav")
