import json
from tkinter import *

import cv2
import numpy as np

from PIL import Image
from PIL import ImageTk

from filter import *

with open ("_INTENSITY.json", "r") as f :
    data = json.load(f)

interface = Tk()
interface.title('get intensity from user')
interface.geometry("800x600")

def get_intensity_test() :
    R, G, B = red_slider.get(), green_slider.get(), blue_slider.get()
    print(f"R:{red_slider.get()}, G:{green_slider.get()}, B:{blue_slider.get()}")

def get_intensity_from_user() :
    R, G, B = red_slider.get(), green_slider.get(), blue_slider.get()
    
    with open("_INTENSITY.json", "r") as f :
        data = json.load(f)

    data[0]['intensity'] = float(R / 100)
    data[1]['intensity'] = float(G / 100)
    data[2]['intensity'] = float(B / 100)

    with open("_INTENSITY.json", "w") as f :
        json.dump(data, f, indent=4)

    interface.destroy()
    
src = cv2.imread("image/image.png")
src = cv2.resize(src, (428, 372))
img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

img = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=img)

label = Label(interface, image=imgtk)
label.pack(side="top")

red_slider = Scale(interface,   label= "RED" ,  from_ = 0, to=100, length=5000, orient=HORIZONTAL)
green_slider = Scale(interface, label= "GREEN", from_ = 0, to=100, length=5000, orient=HORIZONTAL)
blue_slider = Scale(interface,  label= "BLUE",  from_ = 0, to=100, length=5000, orient=HORIZONTAL)

red_slider.pack()
green_slider.pack()
blue_slider.pack()

btn = Button(interface, text = '적용', command=get_intensity_from_user).pack()

interface.mainloop()
