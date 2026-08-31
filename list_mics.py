import sounddevice as sd

print("Recording from USB microphone...")

audio = sd.rec(
    int(5 * 16000),
    samplerate=16000,
    channels=1,
    dtype="int16",
    device=1
)

sd.wait()

print("Recording finished.")
print("Maximum audio level:", abs(audio).max())