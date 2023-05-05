import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
command = "" 
def talk(text):
    engine.say(text)  #text function takes text argument and uses the text -to-speech engine to convert it to speech and play it
    engine.runAndWait()

def take_command():#this function listens to microphone for voice and returns as a string ,this done with the help of recognizer()
    command=None
     # initialize with default value
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            '''  The Listened voice is stored in the variable 'voice'. 
            The 'recognize_google()' method is used to convert the captured voice to text. 
            This method sends the audio to Google's servers, which use machine learning algorithms to transcribe the speech to text. 
            The transcribed text is stored in the variable 'command'.
              The 'lower()' method is then used to convert the text to lowercase for easier processing.'''
            if 'sana' in command:
                command = command.replace('sana', ' ')
                print(command)
    except:
        pass
    return command

def run_sana():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', ' ')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'who is the' in command:
        person = command.replace('who is the',' ')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry , I have a headache')
    elif 'are you single' in command:
        talk('Sorry i am in relationship with sunil')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'tell me about sunil' in command:
        talk(' sunil is from proddatur,kadapa(district) ,India.. Currently he was pursing btech 2-nd year in SREE VIDYANIKETHAN ENGINEERING COLLEGE. and he was aggregated his 10th standard with 10.10 CGPA, and his 12t standard with 96.7 percentage.. his Hobbies are-playing games,Listing muisc,singing songs. his strengths are self motivation & Identifing Mistakes in his self.')
    elif 'bye' in command:
        talk('okay bye')
    elif 'tell me about yourself' in command:
        talk('thank you for asking about me, i am virtual assistance for sunil and i am like a agent but not intelligent agent')
    elif 'how are you' in command:
        talk('As i am assistance for sunil , if he was in happy mood then i am in happy')
    elif 'i love you' in command:
        talk('as a virtual assistance i can not able to show my feelings');
    else:
        talk('please say the command again .!')

while True:
    run_sana()