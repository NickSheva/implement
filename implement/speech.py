"""Make text file from video and audio files"""
from pathlib import Path
from moviepy.editor import *

file_path = Path("MTS.mp4")
if file_path.exists() and file_path.is_file():
    print("Success!")
else:
    print("File does not exist")

