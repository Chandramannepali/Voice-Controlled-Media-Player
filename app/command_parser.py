def parse_command(command_text):
    command_text = command_text.lower()

    if "play" in command_text:
        return "play"
    elif "pause" in command_text:
        return "pause"
    elif "stop" in command_text:
        return "stop"
    elif "volume up" in command_text:
        return "volume_up"
    elif "volume down" in command_text:
        return "volume_down"
    else:
        return "unknown"

