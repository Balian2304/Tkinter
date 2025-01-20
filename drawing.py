import tkinter as tk
from tkinter.colorchooser import askcolor
class Paint():
    THICKNESS = 5
    COLOUR = "black"
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.geometry("500x500")
        self.colorbutton = tk.Button(self.screen,text="Color",command=self.colorfunction)
        self.penbutton = tk.Button(self.screen,text="Pen",command=self.use_pen)
        self.brushbutton = tk.Button(self.screen,text="Brush",command=self.use_brush)
        self.eraserbutton = tk.Button(self.screen,text="Eraser",command=self.use_eraser)
        self.scalebutton = tk.Scale(self.screen,from_=0,to=10,orient="horizontal")
        self.canvas = tk.Canvas(self.screen,bg="white",width=500,height=400)
        self.colorbutton.grid(row=1,column=1)
        self.penbutton.grid(row=1,column=2)
        self.brushbutton.grid(row=1,column=3)
        self.eraserbutton.grid(row=1,column=4)
        self.scalebutton.grid(row=1,column=5)
        self.canvas.grid(row=2,column=1,columnspan=5)
        self.setup()
        self.screen.mainloop()
    def use_pen(self):
        self.activatebutton(self.penbutton)
        self.eraseron = False
    def activatebutton(self,button):
        self.active_button.config(relief = tk.RAISED)
        button.config(relief = tk.SUNKEN)
        self.active_button = button
    def resetbutton(self,event):
        self.old_x,self.old_y = None,None
    def use_eraser(self):
        self.activatebutton(self.eraserbutton)
        self.eraseron = True
    def use_brush(self):
        self.activatebutton(self.brushbutton)
        self.eraseron = False
    def use_color(self):
        self.activatebutton(self.colorbutton)
    
    def colorfunction(self):
        self.colour = askcolor(color=self.colour)[1]
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.thickness = self.THICKNESS
        self.colour = self.COLOUR
        self.active_button = self.penbutton
        self.eraseron = False
        self.canvas.bind("<B1-Motion>",self.paint)
        self.canvas.bind("<ButtonRelease-1>",self.resetbutton)
    def paint(self,event):
        self.thickness = self.scalebutton.get()
        if self.eraseron == True:
            self.paintcolour = "white"
        else:
            self.paintcolour = self.colour
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x,self.old_y,event.x,event.y,fill=self.paintcolour,smooth=True,width=self.thickness,splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y


Paint()
