import time
import pyautogui
import tkinter as tk


def screenshot():
    name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    name = f"C:\\Users\\hp\\Pictures\\Screenshots\\{name}.png"
    time.sleep(1)
    # save screenshot to file in C:\Users\hp\Pictures\Screenshots
    img = pyautogui.screenshot(name)
    img.show()
    print('Screenshot taken')

    # make a gui using tkinter library to display the screenshot and take a screenshot of a specific area

    root = tk.Tk()
    root.title('Screenshot')

    frame = tk.Frame(root, bg='#80c1ff')
    frame.place(relwidth=1, relheight=1)
    frame.pack()

    button = tk.Button(frame, text='Take Screenshot', command=screenshot)
    button.pack(side=tk.LEFT)

    close = tk.Button(frame, text='Quit', command=quit)
    close.pack(side=tk.LEFT)

    root.mainloop()

    # make a gui using tkinter library to display the screenshot and take a screenshot of a specific area
    # write a code to take a screenshot of a specific area and  display it in a gui
root = tk.Tk()
root.title('Screenshot')
root.geometry('500x500')

if __name__ == '__main__':
    screenshot()
