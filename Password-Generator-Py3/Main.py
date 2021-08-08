#importing Libraries
from tkinter import *
import random, string
import pyperclip
from PIL import ImageTk,Image


###initialize window
root =Tk()
root.geometry("420x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

###input icons
photo = PhotoImage(file="./icons/password_500px.png")
root.iconphoto(False,photo);


######picture
img = ImageTk.PhotoImage(Image.open("./icons/lady_window_password_100px.png"))
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "no")


#####heading
heading = Label(root, text = 'RANDOM PASSWORD GENERATOR' , font ='arial 15 bold').pack()
#####footer
Label(root, text ='Copyright © Md. Abdullah Ibna Harun. All rights reserved.', font ='arial 8 bold').pack(side = BOTTOM)


#####select password length
password_label = Label(root, text = 'Chose Password Length', font = 'arial 8 bold').pack()
password_len = IntVar()
length = Spinbox(root, from_ = 6, to_ = 32 , textvariable = password_len, width = 15).pack()



#####define string type variable
password_str = StringVar()
#####define function
def passwordGenerator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(password_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    password_str.set(password)
   


###button
Button(root, text = "GENERATE PASSWORD" , command = passwordGenerator).pack(pady= 10)
###Output
Entry(root , textvariable = password_str).pack()


####function to copy
def copy_password():
    pyperclip.copy(password_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = copy_password).pack(pady=5)



#### loop to run program
root.mainloop()
