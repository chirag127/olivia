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

import tkinter as tk
import sys

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass


print("How can I help you?")

if __name__ == "__main__":

    root = tk.Tk()
    t = tk.Text()
    t.pack()
    # create instance of file like object
    pl = PrintLogger(t)

    # replace sys.stdout with our object
    sys.stdout = pl


    while True:

        root.mainloop()
        
        query = record_audio()
        print("You said: " + query)
