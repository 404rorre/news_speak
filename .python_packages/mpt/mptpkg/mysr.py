import speech_recognition as sr


def voice_to_text():
    """
    Returns text version from speech recognition via NLP.
    """
    voice_input = ""
    speech = sr.Recognizer()

    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio).lower()
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input


if __name__ == "__main__":
    print(voice_to_text())
