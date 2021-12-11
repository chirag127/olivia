import pyaudio
from googletrans import Translator
import speech_recognition as sr
import pyttsx3

# reqiured engine for text to speech

engine = pyttsx3.init('sapi5')

# sapi5 is the default voice engine of windows and it is installed by default in windows

# getproperties is used to get the properties of the engine like rate, volume, pitch, etc.

voices = engine.getProperty('voices')


# setproperties is used to set the properties of the engine like rate, volume, pitch, etc.


engine.setProperty('voice', voices[1].id)

# defining the function to speak the text


def speak(audio):

    engine.say(audio)

    engine.runAndWait()


# defining the function to take command from the user

def takeCommand():

    # create a recognizer object

    r = sr.Recognizer()

    # use the microphone as source for input

    with sr.Microphone() as source:

        # print listening to the user to know that the program is listening

        print("Listening...")

        # refer to the https://www.codesofinterest.com/2017/04/energy-threshold-calibration-in-speech-recognition.html to understand the energy threshold

        # pause for a second to let the recognizer adjust the threshold before listening for input

        r.pause_threshold = 1

        # r.adjust_for_ambient_noise(source, duration=1)

        # r.dynamic_energy_threshold = True

        # r.energy_threshold = 800

        # r.dynamic_energy_adjustment_damping = 0.2

        # listen for the user's input and store it in audio variable and convert it to text later

        audio = r.listen(source)

    try:

        # convert the audio to text

        # print recongzing the user's voice to know that the program is re cognizing the user's voice

        print("Recognizing...")

        # use google translate to detect the language of the user's voice

        query = r.recognize_google(audio, language='en-in')

        # print the user's voice to the console

        print(f"User said: {query}\n")

    # if the user does not say anything then the program will listen again
    except sr.UnknownValueError:

        print("Google Speech Recognition could not understand audio")
        print("Say that again please...")
        return "None"

    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        print("Please Check your internet connection")
        return "None"

    except sr.WaitTimeoutError:
        print("Wait timeout exceeded")
        print("Please Check your internet connection")
        return "None"

    except Exception as e:

        # print the error to the console

        print("Say that again please...")

        # return the function to takeCommand()

        return "None"

    # return the function to takeCommand()

    return query


def sp(text):
    print(text)
    speak(text)


if __name__ == "__main__":

    while True:

        query = takeCommand().lower()

        # telling the user that we are translating the text to the punjabi
        speak("translating")

        # using the goslate library to translate the text
        translator = Translator()

        # translating the text to the punjabi and storing the result in a variable named result
        result = translator.translate(query, dest='ja')
        # speaking and printing the result
        print(result.text)
        speak(result.pronunciation)
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation
                
                speak(result.pronunciation)
