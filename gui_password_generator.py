from tkinter import *
from random import randint

if __name__ == '__main__':

    window = Tk()
    window.title('Password Generator')
    window.configure(background = '#33ccff')
    frame = Frame(window)

    text = Label(window, text = "Here's your password:", font = '14', bg = '#33ccff')

    def randomize():
        characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '1','2','3','4','5','6','7','8','9','0', '?', '*', '$', '#', '!']
    
        char1 = characters[randint(0,67)]
        char2 = characters[randint(0,67)]
        char3 = characters[randint(0,67)]
        char4 = characters[randint(0,67)]
        char5 = characters[randint(0,67)]
        char6 = characters[randint(0,67)]
        char7 = characters[randint(0,67)]
        char8 = characters[randint(0,67)]

        password.set(char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8)
    
    global password
    password = StringVar()
    password.set(' ')
    
    button = Button(frame, text = 'Randomize', command = randomize)
    password_text = Label(window, textvariable = password, font = 'Monospace 24 bold', bg = '#33ccff')

    text.pack(side = TOP)
    button.pack(side = BOTTOM)
    password_text.pack()
    frame.pack(padx = 105, pady = 35)

    window.mainloop()