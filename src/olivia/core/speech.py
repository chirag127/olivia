"""Speech I/O.

TTS  : pyttsx3 / SAPI5 — fully offline (Windows speech engine, no network).
STT  : local faster-whisper (CTranslate2 Whisper) — fully offline. The model
       auto-downloads once from Hugging Face, then transcribes on the CPU with
       no network. Mic audio is captured with sounddevice into a numpy array
       and transcribed locally; nothing is sent to any online service.

Heavy/native imports (pyttsx3, faster_whisper, sounddevice, numpy) are lazy so
this module imports on headless CI without a mic, speaker, or model download.
"""

from olivia.core import config

_engine = None
_whisper = None


# --- Text-to-speech (offline SAPI5) ---


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
    """Say text aloud through the offline SAPI5 voice engine."""
    engine = _get_engine()
    engine.say(str(audio))
    engine.runAndWait()


def sp(text):
    """Print and speak."""
    print(text)
    speak(text)


# --- Speech-to-text (offline local Whisper) ---


def _get_whisper():
    """Load the local faster-whisper model once (downloads on first run, then offline)."""
    global _whisper
    if _whisper is None:
        from faster_whisper import WhisperModel

        _whisper = WhisperModel(
            config.WHISPER_MODEL,
            device=config.WHISPER_DEVICE,
            compute_type=config.WHISPER_COMPUTE_TYPE,
        )
    return _whisper


def _record(seconds=None, sample_rate=None):
    """Capture mono mic audio into a float32 numpy array Whisper can transcribe."""
    import numpy as np
    import sounddevice as sd

    seconds = config.MIC_RECORD_SECONDS if seconds is None else seconds
    sample_rate = config.MIC_SAMPLE_RATE if sample_rate is None else sample_rate
    frames = int(seconds * sample_rate)
    audio = sd.rec(frames, samplerate=sample_rate, channels=1, dtype="float32")
    sd.wait()
    return np.squeeze(audio)


def transcribe(audio):
    """Transcribe a float32 numpy array (16 kHz mono) with local Whisper. Offline."""
    model = _get_whisper()
    segments, _info = model.transcribe(
        audio,
        beam_size=5,
        language=config.WHISPER_LANGUAGE,
    )
    return "".join(seg.text for seg in segments).strip()


def take_command():
    """Record from the mic and transcribe locally. Return text, or 'None' on failure."""
    try:
        print("Listening...")
        audio = _record()
        print("Recognizing...")
        query = transcribe(audio)
        if not query:
            print("No speech detected")
            return "None"
        print(f"User said: {query}\n")
        return query
    except Exception as e:  # mic/model errors shouldn't crash the loop
        print(f"Could not recognize audio: {e}")
        return "None"


# Backwards-compatible alias used across skills.
takeCommand = take_command
