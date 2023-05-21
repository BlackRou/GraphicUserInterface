from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt



root = Tk()
root.title("Learn to code")
root.iconbitmap(r'C:\Users\tomry\GraphicUserInterface\wifi.ico')
root.geometry("400x200")

# Odkaz: https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2
#        https://matplotlib.org/stable/gallery/index.html

# Plots

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 200)
    plt.show()

my_btn = Button(root, text="Graph It!", command=graph)
my_btn.pack()


root.mainloop()