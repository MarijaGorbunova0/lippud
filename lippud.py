import tkinter as tk
from tkinter import *
from turtle import width
from random import choice
raam = tk.Tk()
raam.title("Tahvel")

tahvel = tk.Canvas(raam, width = 600, height = 600, background = "white")
tahvel.grid()


import tkinter as tk

def sahmati():
    root = tk.Tk()
    root.title("")
    cell_size = 60

    canvas = tk.Canvas(root, width=8 * cell_size, height=8 * cell_size)
    canvas.pack()

    colors = ["white", "black"]

    for row in range(8):
        for col in range(8):
            color_index = (row + col) % 2  
            x0, y0 = col * cell_size, row * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[color_index])
    root.mainloop()



def krug():
    OV = tk.Toplevel()
    OV.title("светофор")
    canvas = tk.Canvas(OV, width=600, height=600, bg="white")
    canvas.pack()
    colors = ["black",
              "red",
              "pink",
              "yellow"]
    x0 = 0
    y0 = 0
    x1 = 600
    y1 = 600
    p = 5
    p1 = -5
    for i in range(55):
        x0 += p
        y0 += p
        x1 += p1
        y1 += p1
        canvas.create_oval(x0,y0,x1,y1, fill = choice(colors))

def openSV():
    SV = tk.Toplevel()
    SV.title("светофор")
    canvas = tk.Canvas(SV, width=600, height=600, bg="white")
    canvas.pack()
    
   
    black = canvas.create_rectangle(100, 300, 50, 30, fill="#000000")
    red= canvas.create_rectangle(100, 100, 50, 50, fill="#9e9e9e")
    yellow = canvas.create_rectangle(50, 120, 100, 170, fill="#9e9e9e")
    green = canvas.create_rectangle(50, 184, 100, 220, fill="#9e9e9e")
    
    
    def changeColorRed():
        canvas.itemconfig(red, fill="red")
    def changeColorYellow():  
        canvas.itemconfig(yellow, fill="yellow")
    def changeColorGreen():  
        canvas.itemconfig(green, fill="green") 

        
    canvas.after(4000, changeColorRed)
    canvas.itemconfig(red, fill="#9e9e9e")
    canvas.after(6000, changeColorYellow)
    canvas.after(8000, changeColorGreen)


#eesti
tahvel.create_rectangle(30, 50, 300, 100, fill="#0072CE")
tahvel.create_rectangle(30, 101, 300, 150, fill="#000000")
tahvel.create_rectangle(30, 151, 300, 200, fill="#FFFFFF")

#teine
tahvel.create_rectangle(330, 50, 600, 100, fill = "#078580")
tahvel.create_rectangle(330, 101, 600, 150, fill = "#e3d002")
tahvel.create_rectangle(330, 151, 600, 200, fill = "#078580")
tahvel.create_polygon(330,50,  440,130,  330,200, fill="black")

tahvel.create_rectangle(30, 250, 300, 300, fill = "#f5e21b") 
tahvel.create_rectangle(30, 301, 300, 350, fill = "#55de16")   
tahvel.create_rectangle(30, 351, 300, 400, fill = "#f7310a")



f = Frame(raam)
var = IntVar() #StringVar
svetofor = Radiobutton( f, 
               text = "svetofor",
               variable = var,
               value = 1,
               command = openSV)
oval = Radiobutton( f, 
               text = "oval",
               variable = var,
               value = 2,
               command = krug)
chess = Radiobutton( f, 
               text = "sahmati",
               variable = var,
               value = 3,
               command = sahmati)
#ring
#tahvel.create_rectangle(30,550,  300,300, fill = "red")
#tahvel.create_oval(30,550,  300,300, width = 2, fill="yellow")
x0 = 300
y0 = 300
x1 = 600
y1 = 600
p = 15
p1 = -15
for i in range(12):
    x0 += p
    y0 += p
    x1 += p1 
    y1 += p1
    tahvel.create_rectangle(x0, y0, x1, y1, fill = "red")
    tahvel.create_oval(x0, y0, x1, y1, fill = "yellow")

f.grid(row = 4, column = 0, columnspan = 7)
svetofor.grid(row = 0, column = 0)
oval.grid(row = 2, column = 0)
chess.grid(row = 3, column = 0)    
raam.mainloop()
