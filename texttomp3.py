import os
import pyttsx3

def text_to_audio(text, filename='output.mp3', save_path='file location'):
    # Initialize the Text-to-Speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 130)  # Speed of speech
    engine.setProperty('volume', 1)   # Volume (0.0 to 1.0)

    # Select a male voice
    voices = engine.getProperty('voices')
    for voice in voices:
        if "brave" in voice.name.lower():  # Assuming "brave" is part of the male voice's name
            engine.setProperty('voice', voice.id)
            break

    # Convert text to speech
    engine.save_to_file(text, os.path.join(save_path, filename))
    engine.runAndWait()

# Example text
text = """
example text inside hi how are you MR.SJ 
"""

text_to_audio(text)
