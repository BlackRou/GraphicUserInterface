from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Learn to code")
root.iconbitmap(r'C:\Users\tomry\GraphicUserInterface\wifi.ico')

#button_quit =Button(root, text="Exit Program", command=root.quit)
#button_quit.pack()
# Odkaz: https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2

#r = IntVar()
#r.set("2")

Modes = [
    ("Hawai", "Hawai"),
    ("Cheese", "Cheese"),
    ("Mush", "Mush"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set(" ")

for text, mode in Modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=pizza.get())
    myLabel.pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()


root.mainloop()