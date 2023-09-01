"""Make text file from video and audio files"""
from pathlib import Path
from moviepy.editor import *

file_path = Path("MTS.mp4")
if file_path.exists() and file_path.is_file():
    video = VideoFileClip(f"{file_path}")
    audio = video.audio
    audio.write_audiofile("MTS.wav")
    print("Success")
else:
    print("File does not exist")

