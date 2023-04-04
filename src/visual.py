import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from time import sleep
from btndata import reader
import hid


##TKINTER INIT
window = tk.Tk()
window.title("Ship Console")
window.geometry('1679x1080')
canvas = tk.Canvas(window, width=1679, height=1080)
canvas.pack()

back = Image.open("new.png")
test = ImageTk.PhotoImage(back)

#actual = tk.Label(image=test)
#actual.image = test

canvas.create_image(0, 0, anchor=NW, image=test)
##TKINTER INIT

##NUMBERED, COLORED
def numberBtns(coordsColor):
    lightsColor = []
    lightsNumber = []
    for i, item in enumerate(coordsColor):
        x1,y1,x2,y2 = item
        light = canvas.create_rectangle(x1,y1,x2,y2, fill='')
        label = canvas.create_text((x1+x2)/2, (y1+y2)/2, text=str(i+1), fill='black')
        lightsColor.append(light)
        lightsNumber.append(label)
        canvas.after(500, lambda: [canvas.itemconfig(light, fill='') for light in lightsColor])

##COORDINATES
coordsColor = [(1477, 802, 1547, 868), (1340, 802, 1410, 868), (969, 760, 1039, 825), (1144, 759, 1213, 825), (1057, 759, 1126, 825), (1143, 672, 1212, 738),
                (968, 672, 1038, 738), (1056, 671, 1125, 737), (840, 635, 910, 701), (752, 635, 822, 701), (666, 633, 735, 699), (1058, 584, 1127, 650),
                (838, 495, 907, 561), (751, 495, 820, 561), (665, 494, 734, 560), (838, 415, 908, 481), (751, 415, 821, 481), (664, 414, 734, 480),
                (327, 386, 397, 452), (217, 385, 287, 451), (1034, 112, 1103, 178), (945, 112, 1014, 178), (856, 111, 926, 177), (767, 111, 837, 177),
                (235, 98, 304, 164), (126, 98, 196, 164)]
coord_dict = {}
for i, coord in enumerate(coordsColor):
    coord_dict[i+1] = coord







##THROTTLE PROGRESS BARS
progress_bar_rudder = canvas.create_rectangle(141, 922, 516, 966, fill='green', width=0)
progress_bar_handle1 = canvas.create_rectangle(1302, 272, 1356, 722, fill='green', width=0)
progress_bar_handle2 = canvas.create_rectangle(1553, 280, 1610, 715, fill='green', width=0)

#WIDGETS
scaleRudder = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, length=200)
scaleRudder.pack(side=tk.LEFT, padx=10, pady=10)

scaleHandle1 = tk.Scale(window, from_=0, to=100, orient=tk.VERTICAL, length=200)
scaleHandle1.pack(side=tk.LEFT, padx=10, pady=10)

scaleHandle2 = tk.Scale(window, from_=0, to=100, orient=tk.VERTICAL, length=200)
scaleHandle2.pack(side=tk.LEFT, padx=10, pady=10)


def update_progress_bar_rudder(val):
    max_width = 516 - 141  # maximum width of the progress bar
    val = int(val)
    if val == 0:
        return
    if int(val) == 50:
        coords = (141 + (max_width // 2), 922, 141 + (max_width // 2), 966)
    elif int(val) < 50:
        increment = ((328 - 141) / (50 - 1))
        left_coord = int(141 + increment * (val - 1))
        progress_bar_width = int((328 - 141) / (50 - 1))
        coords = (left_coord, 922, 328, 966)
        print(coords)
    else:
        progress_bar_width = int(float(int(val) - 50) / 50 * (max_width // 2))
        right_coord = 516 - (max_width // 2 - progress_bar_width)
        coords = (right_coord - progress_bar_width, 922, right_coord, 966)
    canvas.coords(progress_bar_rudder, *coords)



def update_progress_bar_handle1(val):
    max_height = 722 - 272  # maximum height of the progress bar
    val = int(val)
    if val == 0:
        y_coordinate = 280
    if int(val) == 50:
        coords = (1302 + (max_height // 2), 280 + max_height, 1356 + (max_height // 2), 280 + max_height)
    elif int(val) < 50:
        slope = (498-280) / 50
        y_coordinate = slope * val + 280
        progress_bar_height = int((722 - 498) / (50 - 1))
        coords = (1302, y_coordinate , 1356, 498)
    else:
        progress_bar_height = int(float(int(val) - 50) / 50 * (max_height // 2))
        bottom_coord = 715 - (max_height // 2 - progress_bar_height)
        coords = (1302, bottom_coord - progress_bar_height, 1356, bottom_coord)
    print(coords)
    canvas.coords(progress_bar_handle1, *coords)


def update_progress_bar_handle2(val):
    max_height = 715 - 280  # maximum height of the progress bar
    val = int(val)
    if val == 0:
        y_coordinate = 280
    if int(val) == 50:
        coords = (1553 + (max_height // 2), 280 + max_height, 1610 + (max_height // 2), 280 + max_height)
    elif int(val) < 50:
        slope = (498-280) / 50
        y_coordinate = slope * val + 280
        progress_bar_height = int((722 - 498) / (50 - 1))
        coords = (1553, y_coordinate , 1610, 498)
    else:
        progress_bar_height = int(float(int(val) - 50) / 50 * (max_height // 2))
        bottom_coord = 715 - (max_height // 2 - progress_bar_height)
        coords = (1553, bottom_coord - progress_bar_height, 1610, bottom_coord)
    print(coords)
    canvas.coords(progress_bar_handle2, *coords)



#START VALUES
scaleRudder.set(50)
scaleHandle1.set(50)
scaleHandle2.set(50)

#UPDATER
scaleRudder.config(command=lambda val: update_progress_bar_rudder(val))
scaleHandle1.config(command=lambda val: update_progress_bar_handle1(val))
scaleHandle2.config(command=lambda val: update_progress_bar_handle2(val))










#LIGHT UP SPECIFIED NUMBER
def lightup(number):
    if number == 0:
        return
    coords = coord_dict[number]
    light = canvas.create_rectangle(*coords, fill='red')
    canvas.after(500, lambda: canvas.itemconfig(light, fill=''))


numberBtns(coordsColor)

##THREADING 
thread = reader()
thread.start()


#UPDATE DISPLAY
def update_display():
    currentNum = thread.get()
    lightup(currentNum)
    canvas.after(10, update_display)

update_display()
window.mainloop()