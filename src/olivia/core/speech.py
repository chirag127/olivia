"""Speech I/O: text-to-speech (pyttsx3/SAPI5) and speech-to-text (Google)."""

from olivia.core import config

_engine = None


def _get_engine():
    global _engine
    if _engine is None:
        import pyttsx3

        _engine = pyttsx3.init("sapi5")
        voices = _engine.getProperty("voices")
        if voices:
            idx = min(config.VOICE_INDEX, len(voices) - 1)
            _engine.setProperty("voice", voices[idx].id)
    return _engine


def speak(audio):
    """Say text aloud through the SAPI5 voice engine."""
    engine = _get_engine()
    engine.say(str(audio))
    engine.runAndWait()


def sp(text):
    """Print and speak."""
    print(text)
    speak(text)


def take_command():
    """Listen on the microphone and return recognized text, or 'None'."""
    import speech_recognition as sr

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition; {e}")
        return "None"
    except sr.WaitTimeoutError:
        print("Wait timeout exceeded")
        return "None"
    except Exception:
        print("Say that again please...")
        return "None"
    return query


# Backwards-compatible alias used across skills.
takeCommand = take_command
