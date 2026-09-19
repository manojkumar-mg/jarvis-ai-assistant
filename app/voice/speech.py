import sounddevice as sd
import speech_recognition as sr
import numpy as np


def listen(
    sample_rate=16000,
    device=1,
    silence_limit=1.2,
    max_duration=8
):
    print("Listening...")

    recognizer = sr.Recognizer()
    audio_chunks = []
    silence_time = 0
    started_speaking = False

    chunk_duration = 0.1
    chunk_size = int(sample_rate * chunk_duration)

    with sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
        device=device,
        blocksize=chunk_size
    ) as stream:

        elapsed = 0

        while elapsed < max_duration:
            audio, overflowed = stream.read(chunk_size)

            audio = audio.flatten()
            audio_chunks.append(audio.copy())

            volume = np.sqrt(np.mean(audio.astype(np.float32) ** 2))

            if volume > 400:
                started_speaking = True
                silence_time = 0
            elif started_speaking:
                silence_time += chunk_duration

            elapsed += chunk_duration

            if started_speaking and silence_time >= silence_limit:
                break

    if not started_speaking:
        return ""

    audio_data = np.concatenate(audio_chunks)

    recognition_audio = sr.AudioData(
        audio_data.tobytes(),
        sample_rate,
        2
    )

    print("Processing...")

    try:
        text = recognizer.recognize_google(recognition_audio)
        return text.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""

    except Exception as error:
        print(f"Speech recognition error: {error}")
        return ""