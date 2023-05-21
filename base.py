from tkinter import *
from PIL import ImageTk,Image



root = Tk()
root.title("Learn to code")
root.iconbitmap(r'C:\Users\tomry\GraphicUserInterface\wifi.ico')

# Odkaz: https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2

def open():
    global my_img
    top = Toplevel()
    top.title("My SCND Window")
    top.iconbitmap(r'C:\Users\tomry\GraphicUserInterface\wifi.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/img1.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="open Second window", command=open).pack()




root.mainloop()