import speech_recognition as sr
from app.text_to_speech import speak
def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for command...")
        speak("Listening for your command")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        speak("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        speak("Speech recognition service is unavailable.")
        return ""
