import speech_recognition as sr

recognizer = sr.Recognizer()

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Trying device {index}: {name}")
    try:
        with sr.Microphone(device_index=index) as source:
            print("  Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("  Say something:")
            audio = recognizer.listen(source, timeout=5)
            print("  Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"✅ Device {index} worked. You said: {text}")
            break
    except Exception as e:
        print(f"❌ Device {index} failed: {e}")
