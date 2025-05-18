import pygame

pygame.mixer.init()

# Set media_file directly to the full path of the mp3 file
media_file = r"C:\Users\purna\OneDrive\Desktop\chandra\music\my_song.mp3.mp3"

def play():
    pygame.mixer.music.load(media_file)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def stop():
    pygame.mixer.music.stop()

def volume_up():
    current_volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(min(current_volume + 0.1, 1.0))

def volume_down():
    current_volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(max(current_volume - 0.1, 0.0))
