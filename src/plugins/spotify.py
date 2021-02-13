import subprocess
from time import sleep
from src import config


def switch_to_light():
    spotify_theme = config.get("spotifyLightTheme")
    if spotify_theme:
        subprocess.run(['spicetify', 'config', 'current_theme', 'Dribbblish', 'color_scheme', spotify_theme]) # Shell theme
        subprocess.run(['spicetify', 'apply'])
        sleep(2.5)
        subprocess.run(['spotify'])

def switch_to_dark():
    spotify_theme = config.get("spotifyDarkTheme")
    if spotify_theme:
        subprocess.run(['spicetify', 'config', 'current_theme', 'Dribbblish', 'color_scheme', spotify_theme]) # Shell theme
        subprocess.run(['spicetify', 'apply'])
        sleep(2.5)
        subprocess.run(['spotify'])
