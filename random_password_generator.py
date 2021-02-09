from tkinter import *
from tkinter.ttk import Combobox
import random
import pyperclip
screen = Tk()
screen.title("Password Generator")
screen.geometry("600x400")
screen.resizable(0,0)

#password generator function
def generate():
    global string
    string.set("")
    password = ""
    length  = int(length_entry.get())
    low_strength = 'abcdefghijklmnopqrstuvwxyz'
    medium_strength = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + low_strength
    high_strength = '0123456789' + low_strength + medium_strength + '!@#$%^&*()-+=?/'
    if selection_box.get() == 'Low':
        for i in range(0, length):
            password = password + random.choice(low_strength)
        string.set(password)   
    elif selection_box.get() == 'Medium':
        for i in range(0, length):
            password = password + random.choice(medium_strength)
        string.set(password)
    if selection_box.get() == 'Strong':
        for i in range(0, length):
            password = password + random.choice(high_strength)
        string.set(password)             


#copy to clipboard function
def copyclip():
    copy_pass = password_box.get()
    pyperclip.copy(copy_pass)
    

string = StringVar("")

#hints for user
label = Label(screen,text= "Note: Please enter only Length and choose Strength", font = ('Arial', 15, 'bold'), fg='darkred')
label.place(x=0,y=0)

#show generated password
label2 = Label(screen, text= 'Password:- ', font = ('Arial', 14))
label2.place(x=145, y=90)
password_box = Entry(screen, font = ('Arial', 14), textvariable = string)
password_box.place(x=255, y=90)

#password length
label3 = Label(screen, text = 'Length:- ', font = ('Arial',14))
label3.place(x=145, y=125)
length_entry = Entry(screen, font = ('Arial',14))
length_entry.place(x=255, y=125)

#passwor strength selection box
label4 = Label(screen, text = 'Strength:- ', font = ('Arial',14))
label4.place(x=145, y=160)
selection_box = Combobox(screen, font = ('Arial',14))
selection_box['values'] = ('Low', 'Medium', 'Strong')
selection_box.current(2)
selection_box.place(x=255, y=160)

#generate button
generate_btn = Button(screen, text='Generate', font = ('Arial',14,'bold'),bg = 'white', fg = 'darkred', command = generate)
generate_btn.place(x=250, y=200)

#copy button
copy_btn = Button(screen, text = 'Copy', font = ('Arial', 12, 'bold'), bg='white', fg='darkred', command = copyclip)
copy_btn.place(x=480, y=86)

screen.mainloop()