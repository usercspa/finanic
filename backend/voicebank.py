import random
import pyttsx3
import speech_recognition as sr
import time
from subprocess import Popen
import twiliogenericsmssender

from bit import PrivateKeyTestnet



##wallet primary (btc)
key = PrivateKeyTestnet('93PC6j7fK4FGyHg4DVXK9f8BnektLqPmyKThDjaJDDZZFbryRNE')
##wallet secondary (btc)
key2 = PrivateKeyTestnet('91uwMrzeW2iWiV8eMj6Y1P8QZhy8Lh4SuD2PQzqxmRx8KSdfbVq')


# idlemovie = 'media/idle_screen.mp4'
# welcomemovie = 'media/welcome_screen_loop.mp4'
# eye1movie = 'media/eyes_open.mp4'
# eye2movie = 'media/eyes_close.mp4'
# fortune1movie = 'media/fortune_1.mp4'
# fortune2movie = 'media/fortune_2.mp4'

## "sudo vlc " + idlemovie +" --no-video-title --loop --fullscreen" 



# omxp = Popen(['omxplayer',idlemovie])

##play idle sequence

password = "coffee"
password2 = "cookies"
usernum = "13218775974"
passphrase = ""

def generate_passphrase():
    words = ['ccokie', 'tea', 'coffee', 'traffic']
    choice =  random.choice(words)
    return choice




maindelay = 5  #delay for main loop

r = sr.Recognizer()


def getSpeech():
    text = "human"
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return text

def speak(sentence):
    eng = pyttsx3.init()
    eng.setProperty('rate', 130) 
    eng.say(sentence)
    eng.runAndWait()
    print(sentence)
    eng.stop() 

# name = input('what is your name?')
# n1 = len(name)

# name = getname()
count = 1

## keyphrase is i like coffee

while (1) :
    count -=1

    ##detect user with distance/motion

    ##led flash


    ## play opening sequence
    # omxp = Popen(['omxplayer', eye1movie])
    
    speak("please speak your password if you have an account, or say open an account to apply for one")
    name = getSpeech()
    name = name.lower()
    if "exit" in name:
    

        speak("goodbye. ")
        break

    if "open" in name and "account" in name:
        details ={}
        speak("please answer the following set of questions")
        speak("what is your legal name")

        data = getSpeech()
        data = data.lower()

        details['name'] = data

        speak("are you above 18 years old?")

        data = getSpeech()
        data = data.lower()

        if 'yes' in data:
            details['adult'] = True
        if 'no' in data:
            details['adult'] = False
        


        speak("are you a united kingdom citizen?")

        data = getSpeech()
        data = data.lower()

        if 'yes' in data:
            details['citizen'] = True
        if 'no' in data:
            details['citizen'] = False



        speak("are you a united kingdom permanent resident?")

        data = getSpeech()
        data = data.lower()

        if 'yes' in data:
            details['resident'] = True
        if 'no' in data:
            details['resident'] = False



        speak("are you a student?")

        data = getSpeech()
        data = data.lower()

        if 'yes' in data:
            details['student'] = True
        if 'no' in data:
            details['student'] = False


        

        speak("what is your gender? you can say male, female or other.")

        data = getSpeech()
        data = data.lower()
        details['gender'] = data

        speak("what is your phone number.")

        data = getSpeech()
        data = data.lower()
        details['gender'] = data

        print (details)

        speak("your details have been recorded. you will soon get a text message with instructions on application and if you qualify. thank you.")

                        
        continue
    
    if password not in name:
        word_list = name.split()
        name = word_list[-1]
        speak("sorry, please try again...")
        continue
    
    speak("greetings.")


    speak("how can i help you today?")
    name = getSpeech()
    name = name.lower()

    if "transfer" in name:
        outstring = "sent with voicebank"
        txid = key2.send([('mkNdHY2qjNqrTG4vqvzYo7kfhqpq22jDeh',0.000001,'btc')],message=outstring)
        print(txid)
        speak("transaction complete.")
        continue

    if "balance" in name:
        # outstring = "sent with voicewallet"
        bal = key2.get_balance('usd')


        speak("the balance in your account is " + str(bal) + " dollars")
        continue

    if "change" in name:
            # outstring = "sent with voicewallet"
        password, password2 = password2, password2


        twiliogenericsmssender.sendtext(usernum, "your new pass phrase is " + password)

        speak("new passphrase generated. please check your text messages. ")
        continue

    if "exit" in name:


        speak("goodbye. ")
        break

    
    
    speak("sorry, i did not understand this command ... ")



    time.sleep(maindelay)

    if count == -4:
        break



