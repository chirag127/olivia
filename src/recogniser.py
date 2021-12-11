from os import times
import speech_recognition as sr

take_command = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = take_command.listen(source)
        voice_data = ''
        try:
            voice_data = take_command.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

print('How can I help you?')
while True:
    voice_data = record_audio()
    print('You said: ' + voice_data)
    