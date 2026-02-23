"""
    Name: jarvis.py
    Author: Paul Gray
    Created: 02/22/26
    Purpose: Learning to run speech recognition 
"""

import speech_recognition as sr  # Assuming you have this
# ... other imports, including from wikipedia_oop ...

# Your existing TTS function, e.g., def speak(text): ...

def get_command():  # Your speech recognition function
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=YOUR_INDEX) as source:  # Use index from troubleshooting
        print("Listening . . .")
        audio = recognizer.listen(source)
        try:
            print("Recognizing . . .")
            command = recognizer.recognize_google(audio).lower()
            return command
        except:
            return None  # Or handle error

# In main loop:
while True:
    print("+---------------------+")
    print("| JARVIS Main Menu    |")
    print("+---------------------+")
    print("Commands: Wikipedia, exit")
    command = get_command()
    if command:
        if "wikipedia" in command:
            print("+---------------------+")
            print("| Search Wikipedia    |")
            print("+---------------------+")
            speak("What would you like to search for on Wikipedia?")  # If TTS
            search_term = get_command()
            if search_term:
                answer = wikipedia_app.get_wikipedia(search_term)
                print(answer)
                speak(answer)  # If TTS
            else:
                print("Google Speech Recognition could not understand what you said.")
        elif "exit" in command:
            print("Goodbye!")
            print("Have a good day!")
            break
    else:
        print("Google Speech Recognition could not understand what you said.")