"""
    Name: jarvis.py
    Author: Paul Gray
    Created: 02/22/26
    Purpose: A program to run speech recognition
"""


import speech_recognition as sr
import pyttsx3
from wikipedia_oop import WikipediaApp

wikipedia_app = WikipediaApp()
engine = pyttsx3.init()

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening . . .")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            print("Recognizing . . .")
            command = recognizer.recognize_google(audio).lower()
            return command
        except:
            return None

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
            speak("What would you like to search for on Wikipedia?")
            
            search_term = get_command()
            if search_term:
                answer = wikipedia_app.get_wikipedia(search_term)
                print(answer)
                speak(answer)
            else:
                print("Could not understand the search term.")
        
        elif "exit" in command:
            speak("Goodbye!")
            break
    else:
        print("Could not understand the command.")