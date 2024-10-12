from gtts import gTTS
from moviepy.editor import *
import os

# Get the current working directory
current_folder = os.getcwd()

# Define the file names for the input text, image, audio, and output video
input_file_name = 'inputscript.txt'
image_file_name = 'image.png'
output_audio_name = 'output_audio.mp3'
output_video_name = 'output_video.mp4'

# Define full paths based on the current folder
input_file_path = os.path.join(current_folder, input_file_name)
image_file_path = os.path.join(current_folder, image_file_name)
output_audio_path = os.path.join(current_folder, output_audio_name)
output_video_path = os.path.join(current_folder, output_video_name)

# Step 1: Convert the text to speech (generate mp3)
print("Generating audio...")
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Convert the text to speech
tts = gTTS(text, lang='hi')  # 'hi' for Hindi language
tts.save(output_audio_path)  # Save the audio as an MP3 file
print(f"Audio file saved at: {output_audio_path}")

# Step 2: Wait for the audio generation to complete and then create the video
print("Generating video...")

# Load the audio and image files
audio = AudioFileClip(output_audio_path)
image = ImageClip(image_file_path).set_duration(audio.duration)

# Set the audio to the image
video = image.set_audio(audio)

# Set the video properties (size, fps)
video = video.set_fps(24)

# Write the final video file
video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

# Confirm the save
print(f"Video file saved at: {output_video_path}")
