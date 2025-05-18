from app.voice_controller import listen_for_command
from app.command_parser import parse_command
from app.media_controller import play, pause, stop, volume_up, volume_down
from app.text_to_speech import speak


def main():
    speak("Voice-controlled media player is ready.")
    while True:
        command_text = listen_for_command()
        intent = parse_command(command_text)

        if intent == "play":
            play()
            speak("Playing media.")
        elif intent == "pause":
            pause()
            speak("Paused.")
        elif intent == "stop":
            stop()
            speak("Stopped playback.")
        elif intent == "volume_up":
            volume_up()
            speak("Volume up.")
        elif intent == "volume_down":
            volume_down()
            speak("Volume down.")
        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
