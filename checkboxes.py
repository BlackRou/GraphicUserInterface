from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title("Learn to code")
root.iconbitmap(r'C:\Users\tomry\GraphicUserInterface\wifi.ico')

# Odkaz: https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2


def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text ="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
# Glitch we need to deselect..
c.deselect()
c.pack()

mybtn = Button(root, text="Show Selection", command=show).pack()


root.mainloop()