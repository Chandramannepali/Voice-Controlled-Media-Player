import app.voice_controller

print("✅ FILE LOADED:", app.voice_controller.__file__)
print("✅ FUNCTIONS & VARIABLES:")
print(dir(app.voice_controller))

print("\n✅ listen_for_command exists:", hasattr(app.voice_controller, "listen_for_command"))
