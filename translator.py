from tkinter import *
import tkinter
from tkinter.font import Font
 
# defining the window
root = Tk()
root.title('Aurebesh Translator')
root.geometry('500x500')
icon1 = PhotoImage(file = 'Aurek.png')
root.iconphoto(False, icon1)

# the aurebesh font
aurebesh = Font(family='Aurek-Besh', size=24)
english = Font(family='Star Jedi', size=24)

# the aurebesh output  
def translateToAurebesh():
    outputAurebesh = Label(root, text=eEnglish.get(), font=aurebesh)
    outputAurebesh.pack()

# translates from english to aurebesh
eEnglish = tkinter.Entry(root, width = 50)
aurebeshTranslateButton = tkinter.Button(root, text='Translate', command=translateToAurebesh)

def eToAScreen():
    clearStartPage()
    eEnglish.pack()
    aurebeshTranslateButton.pack()

# the english output
def translateToEnglish():
    outputEnglish = Label(root, text=eAurebesh.get(), font=english)
    outputEnglish.pack()

# command to place the aurebesh letter
def placeLetter():
    eAurebesh.insert(0, string='a')

# translates from aurebesh to english
eAurebesh = tkinter.Entry(root, width = 50)
englishTranslateButton = tkinter.Button(root, text = 'Translate', command=translateToEnglish)
letterA = Button(root, text='A', font=aurebesh, command=placeLetter)

def aToEScreen():
    clearStartPage()
    eAurebesh.pack()
    englishTranslateButton.pack()
    letterA.pack()

# prints the start page
englishToAurebesh = Button(root, text='English to Aurebesh', command=eToAScreen)
aurebeshToEnglish = Button(root, text='Aurebesh to English', command=aToEScreen)

def startPage():
    englishToAurebesh.pack()
    aurebeshToEnglish.pack()

def clearStartPage():
    englishToAurebesh.destroy()
    aurebeshToEnglish.destroy()

startPage()

root.mainloop()
  

  

