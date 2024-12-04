from pytoon.animator import animate
from pprint import pprint

from moviepy.editor import (
    ImageClip,
)

FPS = 48
text_path = "./.test/speech.txt"  #  txt file with transcript text
audio_path = "./.test/speech.mp3"  #  audio file of speech

# Load the transcript
with open(text_path, "r") as file:
    transcript = file.read()

# Generate the cartoon animation of the character saying the words in audio file
animation = animate(audio_file=audio_path, transcript=transcript)

video_clip = ImageClip("./.test/image.png")
video_clip.set_fps(FPS)
video_clip.duration = animation.duration

animation.export(path="./output_animation.mp4", background=video_clip)