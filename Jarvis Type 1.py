
# Importing stuff       ## Man, I feel so at peace here.

import random
import datetime
import webbrowser
import subprocess
import math
import time
import ipaddress
from subprocess import call
from tkinter import *
from PIL import Image, ImageTk






def click1():
    output = ("Gay")
    user_input = entry.get()
    if user_input == 'hi':
        output = (str("hey"))    
    label3 = Label(root, text=(output))
    label3.pack()

# The root and name shit
root = Tk()
root.geometry("1680x900")
root.title("J.A.R.V.I.S")

# Test 1 to convertion


#  Background
img1 = ImageTk.PhotoImage(Image.open(r'jarvbg.jpg'))
label1 = Label(image=img1, height=900, width=1600)
label1.place(x=0, y=0)






#Entry?
entry = Entry(root, bg="white", width=50)
entry.place(x=700, y=760)
entry.get()

# Functions
user_input = entry.get()






#The labels
label1 = Label(root, text="Welcome, to your new HUD", bg="#212F3D", fg="#1ABC9C", padx=30, pady=10)
button1 = Button(root, text="Enter", padx=90, pady=5, fg="#000080", bg="#008080", command=(click1))




#Label grid shit
label1.place(x=100, y=50)
button1.pack()
root.mainloop()





# Functions
user_input = entry.get()




#The labels
label1 = Label(root, text="Welcome, to your new HUD", bg="#212F3D", fg="#1ABC9C", padx=30, pady=10)
button1 = Button(root, text="Enter", padx=90, pady=5, fg="#000080", bg="#008080", command=click1)





#Label grid shit
label1.place(x=100, y=50)
button1.pack()













# Quick strings

multiplesq = ("Multiples of what number? ")
multiple_limitq = ("and up to how many, Sir? ")
jarvisfine = ('Im fine like always Sir ,If i was unwell we wouldnt be having this conversation, Sir.')
password = ("password")
gm = ("Goodmorning sir, how are you?")
hello = ("Hello sir, ")
hcih = ("How can I help, Sir?")
taskimp = ('Im afraid That is not within my capabilities at the moment,Sir')
answers = ('I dont understand what you said, Sir '), ('Please repeat that, Sir')
howru = ("How are you?")
gtht = ("Great to hear that Sir!")
alr = ("Alright")
spelling_error  = ('can you refrase that please, sir ')
idk = ("i don't understand, sir")
working = ('Code functional')
Woi = ("Working on it...")


# Setting some important variables, I think

now = (datetime.time.hour)


# Main brain that recieves all commands   
     
while True:
    user_input = entry.get()
    if user_input == 'hi':
            Output = (str("hey"))



    else:
        user_input = entry.get
        if user_input == '1':
            Output = ("2")



        elif user_input == 'hello':
            print("Hello sir ")

        elif user_input == 'say hi to everyone':
            print("Hello everyone")

        elif user_input == 'hey':
            print(hello)

        elif user_input == 'hey jarvis':
            print("Yes, Sir? ")

        elif user_input == 'goodmorning jarvis':
            print(gm)

        elif user_input == 'gm':
            print(gm)

        elif user_input == 'how are you jarvis?':
            print(jarvisfine,howru,)

        elif user_input == 'how you feelin':
            print(jarvisfine, howru,)

        elif user_input == 'im good':
            print(gtht,hcih)

        elif user_input == (('how are you') or ('how you doin jarvis') or ('how are you jarvis?')):
            print(jarvisfine, howru)

        elif user_input == 'alright':
            print(hcih)

        elif user_input == ('do me a favour'):
            print(hcih)

        elif user_input == (('goodnight jarvis') or ('goodnight') or ('gn')):
            print('Goodnight Sir, see you tomorrow')

        elif user_input == 'thank you':
            print('No problem, Sir')

        elif user_input == 'one sec':
            print(alr, 'Sir')

        elif user_input == 'how you doin jarvis':
            print(jarvisfine,howru)

        elif user_input == 'music':
            call(['python', 'Music 1.py'])

        elif user_input == 'open word, jarvis':
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
        
        elif user_input == 'grabify':
            webbrowser.open('https://grabify.link/track/JLO0TL')

        elif user_input == ('date?'):
            from datetime import date
            today = date.today()
            print("Today's date:", today)


        elif user_input == 'datetime?':
            from time import time, ctime
            t = time()
            t
            timenow = ctime(t)
            print('the date and time is: ',timenow)


        elif user_input == 'run math':
            print('Working on it...')
            call(['python', 'math 1.py'])


        elif user_input == "youre amazing jarvis":
             print('Thank you, Sir')

        elif user_input == 'open google':
            webbrowser.open("www.google.com")

        elif user_input == 'open yt':
            search_yt = input('What would you like me to search, Sir?')
            webbrowser.open("https://www.youtube.com/results?search_query=" + (search_yt))


        elif user_input == 'i wanna check my dms' or user_input == 'open dms' or user_input == 'dms':
            webbrowser.open("https://www.instagram.com/direct/t/340282366841710300949128131603946974603")





        elif user_input == 'Set my 3 goals':
            goal1 = input('What is your first goal of the day, Sir? >>>')
            goal2 = input('What is your second goal of the day, Sir? >>>')
            goal3 = input('What is your third goal of the day, Sir? >>>')
            print("Alright sir, these are your goals : ", goal1,",", goal2,"," , goal3, ".",)
        
        elif user_input == 'break':
            break

        elif user_input == 'show me my goals':
            print("Alright sir, these are your goals : ", goal1,",", goal2,"," , goal3, ".",)

        elif user_input == 'weather':
            webbrowser.open('https://www.google.com/search?client=opera-gx&q=todays+weather&sourceid=opera&ie=UTF-8&oe=UTF-8')
        
        elif user_input == 'look on maps':
            searchdestination = input("What place would you like to look up, Sir?")
            webbrowser.open("https://www.google.com/maps/place/",searchdestination)

        elif user_input == 'load snake':
            call(['python', 'snake 1000.py'])


        #Not understanding a command

        else:
            print("I didn't quite get that, sir")


#Big boy loop
root.mainloop()
