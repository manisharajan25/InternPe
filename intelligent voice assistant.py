import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import datetime
import wikipedia
import os

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = p.init()
rate=engine.getProperty('rate')  #getting voice speed by default
engine.setProperty('rate', 150)    #setting voice speed manually
voices=engine.getProperty('voices')   #getting voice
engine.setProperty('voice', voices[1].id) #setting voice male/female using index offered by my os

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

print("Assist: Hello mam, I'm your voice assistant. How are you?")
speak("Hello mam, I'm your voice assistant. How are you?")

# To listen to user's voice command
def take_command():
    with sr.Microphone() as source:
        recognizer.energy_threshold=10000 #bg property (energy_threshold): it increases the spectrum of a voice (if we increase it, it will capture even low voices)
        recognizer.adjust_for_ambient_noise(source,1.2) #bg property (adjust_for_ambient_noise): cancels all the noises around you (will capture just your voice)
        print("Listening...")
        recognizer.pause_threshold = 1
        audio =recognizer.listen(source) #it listens to what we say and captures in microphone and saves the 'audio' in the variable we have mentioned here
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand, please say that again...")
        return None
    return query.lower()

# Main function for handling voice commands
def assistant():
    while True:
        query = take_command()
        if query is None:
            continue
        
        # Commands and their responses
        elif "what" and "about" and "you" in query:
            print("I'm having a good day mam")
            speak("I'm having a good day mam")
            print("What can I do for you??")
            speak("What can I do for you??")

        elif "open google" in query:
            print("Opening Google")
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        
        elif "time" in query:
            time_now = datetime.datetime.now().strftime("%H:%M")
            print(f"Assist: The current time is {time_now}")
            speak(f"The current time is {time_now}")
        
        elif "tell" and "me" and "about" in query:
            query = query.replace("tell me about", "")
            info = wikipedia.summary(query, sentences=2)
            print(f"Assist: According to Wikipedia, {info}")
            speak(f"According to Wikipedia, {info}")
        
        elif "exit" in query:
            print("Assist: Goodbye!")
            speak("Goodbye!")
            break

# Run the assistant
assistant()























