import secrets
import string
from tkinter import *
import requests
from PIL import Image, ImageTk

# Create strings for the characters that can be part of the password

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars
pwd_length = 12

# Create a function that randomly goes through and picks out characters to put into the password

def random_pass():

    pwd = ''
    for i in range(pwd_length):
     pwd += ''.join(secrets.choice(alphabet))


    def print_pass():
        print(pwd)

# Print Password

    print_pass()

# Create a "GUI" to make it easier to generate a password

def GUI():

    window=Tk()

    # Widgets here
    btn=Button(window, text="Generate Password", fg='black', command = random_pass)
    btn.place(x=100, y=80)
    #
    window.title('PassGen')
    window.geometry("300x200+10+10")
    window.mainloop()

# Run the GUI that enables you to generate passwords

GUI()