from tkinter import *

root = Tk()

def myclick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()



myButton = Button(root, text="Click me!", command=myclick)# fg="blue", bg="#000000"- HEX colors (CSS) #state=DISABLED, padx=50, pady=50
myButton.pack()

root.mainloop()