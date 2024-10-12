# Vettaiyan Movie Review in Hindi | Why Rajinikanth’s Latest is a Must-Watch Before *Singham Again*!  
[Watch the sample video on YouTube](https://youtu.be/dR3eo_gK48U?si=4QpZ-UiYPTbpKDNz)

## Project Overview
This project automates the process of generating a movie review video from a text script and a static image, combining audio and visual elements. The tool converts the provided movie review script into an audio file using Google Text-to-Speech (gTTS) and then combines this audio with a static image to create a professional-looking video, ready for sharing on platforms like YouTube.

The project was used to generate a review for the movie *Vettaiyan*, focusing on why Rajinikanth’s latest movie is a must-watch before *Singham Again*. You can check out the generated video on YouTube:  
[Watch the video](https://youtu.be/dR3eo_gK48U?si=4QpZ-UiYPTbpKDNz)

## Features
- **Text-to-Audio Conversion**: The tool reads a Hindi script and converts it into a high-quality MP3 audio file.
- **Audio and Image to Video**: The generated audio is combined with a static image (such as a movie poster or related image) to create an engaging video with background sound.
- **Completely Automated**: Once set up, the process runs automatically with minimal manual intervention, making it perfect for quick content creation.
  
## Folder Structure
Here’s how the project is structured:

```
Vettaiyan-Movie-Review/
│
├── inputscript.txt             # The movie review script in Hindi (text format)
├── image.png                   # A static image (e.g., a poster or still from the movie)
├── output_audio.mp3            # The generated audio file (Hindi narration)
├── output_video.mp4            # The final video file (audio + image combined)
├── converter.py                # Python script that automates the conversion process
├── README.md                   # Documentation of the project
├── LICENSE                     # License file specifying usage rights
└── requirements.txt            # List of required Python libraries
```

### File Descriptions:
- **inputscript.txt**: Contains the text of the movie review (in Hindi) that will be converted into an audio file. You can replace this with your own review script for other movies or content.
  
- **image.png**: A high-resolution static image, such as a poster of the movie *Vettaiyan* or any related visual that will be used as the background of the video. The image should be in PNG or JPG format.

- **output_audio.mp3**: The generated audio file, where the text from `inputscript.txt` is read aloud in Hindi using the Google Text-to-Speech API.

- **output_video.mp4**: The final video combining the static image (`image.png`) and the generated audio (`output_audio.mp3`). This video is suitable for sharing on YouTube or other video platforms.

- **converter.py**: The main script that handles both the conversion of text to audio and the creation of the final video. It automates the entire process and ensures that the video is generated once the audio is fully developed.

- **README.md**: This documentation file provides instructions on how to set up and use the project. It includes installation instructions and usage examples.

- **LICENSE**: Specifies the license governing the use of this code, outlining any restrictions or allowances for other users.

- **requirements.txt**: Lists all the Python libraries and dependencies needed to run the project (e.g., `gTTS`, `moviepy`). This file makes it easy to install all the necessary libraries by running a single command.

## How It Works
1. **Input Script**: The project starts with a pre-written movie review script in Hindi. The script is stored in `inputscript.txt`, and this is the content that will be turned into audio.
  
2. **Text-to-Speech Conversion**: The text from `inputscript.txt` is processed by Google Text-to-Speech (gTTS) to produce a high-quality MP3 file in Hindi, narrating the movie review.

3. **Image and Audio to Video**: Once the audio is ready, the script combines the MP3 file with a static image (provided as `image.png`) to create a simple yet effective video that can be shared online. The resulting video is saved as `output_video.mp4`.

4. **Final Output**: The final product is a polished video where the review is narrated over a static background image, similar to content shared on YouTube or other video platforms.

## Setup Instructions

### Prerequisites
- **Python 3.x** installed on your machine.
- Basic knowledge of using the command line or terminal.

### Step-by-Step Instructions

1. **Clone the Repository**:
   First, download the project from the GitHub repository or clone it to your local machine:
   ```bash
   git clone https://github.com/DennyM55/text-to-audio-video-converter.git
   ```

2. **Install Dependencies**:
   Install the necessary Python libraries using `pip` and the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Customize the Script**:
   - Update `inputscript.txt` with your own movie review in Hindi (or any other language).
   - Replace `image.png` with a new image if you want a different background.

4. **Run the Script**:
   Execute the script to generate both the audio and video:
   ```bash
   python converter.py
   ```

5. **Find the Output**:
   After the script runs, the generated `output_audio.mp3` and `output_video.mp4` files will be saved in the same folder. The video is ready to be uploaded to platforms like YouTube!

## Sample Output
Check out the sample video generated using this tool:  
[Watch the Vettaiyan Movie Review](https://youtu.be/dR3eo_gK48U?si=4QpZ-UiYPTbpKDNz)

## Conclusion
This project provides a simple, automated solution for generating engaging movie review videos using text scripts and static images. It’s an excellent tool for content creators who want to streamline their workflow and quickly produce video content with minimal effort.

Feel free to replace the text and images to create your own video reviews, tutorials, or any other content format. You can easily scale this project for various use cases, such as educational videos, product reviews, and more!

---
Enjoy creating your own videos with this easy-to-use script!
