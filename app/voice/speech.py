import sounddevice as sd
import speech_recognition as sr


def listen(duration=5, sample_rate=16000):
    print("Listening...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
        device=1
    )

    sd.wait()

    audio_data = sr.AudioData(
        audio.tobytes(),
        sample_rate,
        2
    )

    recognizer = sr.Recognizer()

    try:
        text = recognizer.recognize_google(audio_data)
        return text.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""

    except Exception as error:
        print(f"Speech recognition error: {error}")
        return ""