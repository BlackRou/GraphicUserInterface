from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Learn to code")
root.iconbitmap(r'C:\Users\tomry\GraphicUserInterface\dronmove.ico')

#button_quit =Button(root, text="Exit Program", command=root.quit)
#button_quit.pack()
# Odkaz: https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2

my_img1 = ImageTk.PhotoImage(Image.open("images/img1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.png"))

image_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1))

    if image_num == 4: 
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image "+ str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1))

    if image_num == 1: 
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update status Bar
    status = Label(root, text="Image "+ str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()