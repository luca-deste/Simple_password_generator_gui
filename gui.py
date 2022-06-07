import tkinter as tk
from passCreator import generatePassword

window = tk.Tk()

def newPassword():
    label['text'] = generatePassword()

def copyToClippboard():
    window.clipboard_clear()
    window.clipboard_append(label['text'])

label = tk.Label(text=generatePassword(),
    width=20,
    height=10)
label.pack()
button = tk.Button(text='New Password',
command=newPassword)
copyButton = tk.Button(text='Copy Password',
command=copyToClippboard)
button.pack()
copyButton.pack()
window.mainloop()