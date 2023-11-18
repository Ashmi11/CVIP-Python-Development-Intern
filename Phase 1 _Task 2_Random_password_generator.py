import random
from tkinter import *

# Creation of GUI
root = Tk()
root.title('Random Password Generator')
root.geometry('1000x700')
root.config(bg='bisque1')
root.resizable(0,0)


# Some pre-written characters to give a system generated random password to user

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_-+='
characters = alpha + numbers + symbols


# Function to create the random password using the length and characters input by the user
def generate_password():
    user_info = user_wish.get()
    length = character_length.get()
    password = "".join(random.sample(user_info, int(length)))
    label_password.config(text='Generated Random Password  :' + password)


# Function to create random password using the available characters and user length input
def generate_password2():
    length = character_length2.get()
    password = "".join(random.sample(characters, int(length)))
    label_password2.config(text='Generated Random Password :' + password)


# Heading for the first choice for users

label_heading1= Label(root, text= "To use characters of your choice to Generate password enter the following:", font=('Densia sans',16),bg='light blue',fg='dark blue').pack(padx=10,pady=30)


# Creates a field for user to input of length of password desired

label_characters = Label(root, text="Number of characters", font=('Arial', 14),bg='light pink', fg='crimson').pack(padx=10,pady=10)
character_length = Entry(root, font="Arial 14")
character_length.pack(padx=10,pady=10)


# Creates a field for user to enter any random characters they wish to create the password with

label_user_wish = Label(root,text="Enter any Character you want in the password", font=('Arial', 14),bg='light pink',fg='crimson').pack(padx=10)
user_wish = Entry(root, font="Arial 14")
user_wish.pack(padx=10,pady=10)



# Button to display output whhich calls the function generate_password to display password with characters and length of user's choice

Button(root, text="Generate Password ", command=generate_password, font=('Arial', 16),bg='light yellow',fg='dark blue').pack(padx=10,pady=20)
label_password = Label(root, font=('Arial', 18),bg='lavender')
label_password.pack()


# Heading for the users to know the second option

label_heading1= Label(root, text= "To use unknown characters in system to Generate password enter the following:", font=('Densia sans',16),bg='light blue',fg='dark blue').pack(padx=10,pady=30)


# Creates a field for user input of length of password desired

label_characters2 = Label(root, text="Number of characters", font=('Arial', 14),bg='light pink',fg='crimson').pack(padx=10)
character_length2 = Entry(root, font="Arial 14")
character_length2.pack(padx=10,pady=10)


# Button to desplay output and call function generate_password2 which creates password with avalaible characters in code and length specified by users

Button(root, text="Generate Password", command=generate_password2, font=('Arial', 14),bg='light yellow', fg='dark blue').pack(padx=10,pady=20)
label_password2 = Label(root, font=('Arial', 20),bg='lavender')
label_password2.pack()

root.mainloop()