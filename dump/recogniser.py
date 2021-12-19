from os import times
import speech_recognition as sr

take_command = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = take_command.listen(source)
        voice_data = ""
        try:
            voice_data = take_command.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Sorry, my speech service is down")
        return voice_data


print("How can I help you?")
while True:
    query = record_audio()
    print("You said: " + query)

    query = query.replace("increase volume by", "")
    query = query.replace("volume up by", "")
    query = query.replace("louder", "")

    if "percent" in query or "percentage" in query or "%" in query:
        query = query.replace("percent", "")
        query = query.replace("percentage", "")
        query = query.replace("%", "")

        # volume is increased by the number of percentage mentioned in the query
        # volume is increased by 5 percentage by one up press
        # volume is increased by 10 percentage by two up presses
        # volume is increased by 15 percentage by three up presses
        # volume is increased by 20 percentage by four up presses
        # volume is increased by 25 percentage by five up presses

        query = query.replace(" ", "")
        percent = int(query)

        no_of_up_presses = int(percent / 5)
        for i in range(no_of_up_presses):
            print("up")
