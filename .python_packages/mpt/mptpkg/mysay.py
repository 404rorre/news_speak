# Module Text to speech for Windows

import pyttsx3


def _init_speach_module(language="en_EN", gender="VoiceGenderFemale"):
    # Initializing and setup text to speech
    try:
        engine = pyttsx3.init()
    except ImportError:
        pass
    except RuntimeError:
        pass
    voices = engine.getProperty("voices")
    # language for voice engine
    if language == "en_EN":
        engine.setProperty("voice", voices[1].id)
    else:
        for voice in voices:
            if language in voice.languages and gender == voice.gender:
                engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.2)

    # returns setup voice engine
    return engine


def print_say(txt, language="en_EN", gender="VoiceGenderFemale"):
    """Taking prompt and transforming to voice."""
    engine = _init_speach_module(language, gender)
    print(txt)
    engine.say(txt)
    engine.runAndWait()
