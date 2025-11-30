import speech_recognition as sr 
import pyttsx3 
import logging 
import os 
import datetime 
import wikipedia 
import webbrowser 
import random 
import subprocess 


# Logging configuration 
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)



# Activating voice from our system 
engine = pyttsx3.init("sapi5") 
engine.setProperty('rate', 190)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


# This is speak function
def speak(text):
    """This function converts text to voice

    Args:
        text
    returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()



# This function recognize the speech and convert it to text 

def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"
    
    return query


def greeting():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir! How are you doing?")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir! How are you doing?")
    else:
        speak("Good Evening sir! How are you doing?")
    
    speak("I am MAISARA. Please tell me how may I help you today?")


greeting()

while True:
    query = takeCommand().lower()
    print(query)

    if "your name" in query:
        speak("My name is MAISARA")
        logging.info("User asked for assistant's name.")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {strTime}")
        logging.info("User asked for current time.")

    
    # Small talk
    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")
        logging.info("User asked about assistant's well-being.")
    
    elif "who made you" in query:
        speak("I was created by Bappy sir, a brilliant mind!")
        logging.info("User asked about assistant's creator.")
    
    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("User expressed gratitude.")
    
    elif "open google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")
        logging.info("User requested to open Google.")

        
    # Calculator
    elif "open calculator" in query or "calculator" in query:
        speak("Opening calculator")
        subprocess.Popen("calc.exe")
        logging.info("User requested to open Calculator.")
        

     # Notepad
    elif "open notepad" in query:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        logging.info("User requested to open Notepad.")

   
    # Calendar
    elif "open calendar" in query or "calendar" in query:
        speak("Opening Windows Calendar")
        webbrowser.open("https://calendar.google.com")
        logging.info("User requested to open Calendar.")

    
    # YouTube search
    elif "youtube" in query:
        speak("Opening YouTube for you.")
        query = query.replace("youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        logging.info("User requested to search on YouTube.")

    
    elif "open facebook" in query:
        speak("ok sir. opening facebook")
        webbrowser.open("facebook.com")
        logging.info("User requested to open Facebook.")

    
    elif "open github" in query:
        speak("ok sir. opening github")
        webbrowser.open("github.com")
        logging.info("User requested to open GitHub.")

    
    # Jokes
    elif "joke" in query:
        jokes = [
            "Why don't programmers like nature? Too many bugs.",
            "I told my computer I needed a break. It said no problem, it will go to sleep.",
            "Why do Java developers wear glasses? Because they don't C sharp."
        ]
        speak(random.choice(jokes))
        logging.info("User requested a joke.")

    
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User requested information from Wikipedia.")

    # send message to WhatsApp
    elif "send message" in query:
        speak("Whom do you want to send?")
        name = takeCommand()

        speak("What is the message?")
        message = takeCommand()

    # Add numbers of people in your contact database
        contacts = {
            "kabir": "+8801817182551",
            "khaleda": "+8801817182551",
            "boss": "+8801817182551"
        }

        if name.lower() in contacts:
            send_whatsapp(contacts[name.lower()], message)
            speak("Message sent successfully.")
        else:
            speak("Sorry, I don't have that contact.")

    
    elif "exit" in query:
        speak("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited the program.")
        exit()

        
    else:
        speak("I am sorry, I can't help you with that.")
        logging.info("User asked for an unsupported command.")