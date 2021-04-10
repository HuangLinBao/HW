from tkinter import *
from typing import Tuple
from PIL import Image
from PIL import ImageTk
from tkinter import Button, Tk, filedialog,messagebox,Label
import PIL
import cv2
import numpy as np

class Hw(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('HW')
        #self.resizable(0,0)


        #Widgets
        self.openSaveFrame = Frame(self)
        self.openSaveFrame.pack()
        self.imageLabel = Label(self)
        self.imageLabel.pack()
        self.openImage('goku.png')
        self.buttonframe = Frame(self)
        self.buttonframe.pack()


        self.openImg = Button(self.openSaveFrame,text='Open', command=self.openImage).pack(fill=BOTH,side=LEFT, padx=100)
        self.saveImg = Button(self.openSaveFrame,text='Save', command=self.saveImage).pack(fill=BOTH,side = RIGHT,padx=100)
        self.brightnessLabel = Label(self.buttonframe).pack(fill=BOTH,side = LEFT)
        self.brightnesText = Label(self.brightnessLabel,text='Brightness: ').pack(side=LEFT)
        self.brightDown = Button(self.brightnessLabel, text = '<',      command=lambda: self.brightness('DOWN') ).pack(side=LEFT)
        self.brightUp = Button(self.brightnessLabel, text = '>',        command=lambda: self.brightness('UP')   ).pack(side=LEFT)
        self.contrastLabel = Label(self.buttonframe).pack(fill=BOTH)
        self.contrastUp = Button(self.contrastLabel, text = '>',        command=lambda: self.contrast('UP') ).pack(side=RIGHT)
        self.contrastUp = Button(self.contrastLabel, text = '<',        command=lambda: self.contrast('DOWN') ).pack(side=RIGHT)
        self.contrastText = Label(self.contrastLabel,text='Contrast: ').pack(side=RIGHT)
        self.otherButtonsLabel = Label(self.buttonframe).pack(side=BOTTOM)
        self.seperator = Label(self.otherButtonsLabel ).pack()
        self.seperator = Label(self.otherButtonsLabel ).pack()
        self.seperator = Label(self.otherButtonsLabel ).pack()
        self.seperator = Label(self.otherButtonsLabel ).pack()
        self.revertButton = Button(self.otherButtonsLabel, text='Revert Back', command=self.revertImage).pack(side=LEFT)
        self.bitPlane = Button(self.otherButtonsLabel, text='Extratc Bit Planes').pack(side=RIGHT)
        self.thresholdingLabel = Label(self.buttonframe).pack()
        self.seperator1 = Label(self.thresholdingLabel ).pack()
        self.seperator1 = Label(self.thresholdingLabel ).pack()
        self.seperator1 = Label(self.thresholdingLabel ).pack()
        self.seperator1 = Label(self.thresholdingLabel ).pack()
        self.val1 = Scale(self.thresholdingLabel, from_=0, to=255, orient=HORIZONTAL)
        self.val1.pack(side=LEFT,padx=10)
        self.val2 = Scale(self.thresholdingLabel, from_=0, to=255, orient=HORIZONTAL)
        self.val2.pack(side=LEFT,padx =10)
        self.threshButton =Button(self.thresholdingLabel,text='Threshold', command= lambda: self.mythreshold(int(self.val1.get()),int(self.val2.get()))).pack(padx=10)




        

 

    #methods
    def updateLabel(self, img):
        tempImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        tempImg = PIL.Image.fromarray(tempImg)
        tempImg = PIL.ImageTk.PhotoImage(image=tempImg)
        self.imageLabel.configure(image=tempImg)
        self.imageLabel.image = tempImg
   
    def openImage(self, filename=None):
        if filename is None:	# if the filename was not passed as a parameter
    			    try:
    				    filename = filedialog.askopenfilename(initialdir='~/Pictures',title='Open image') #, filetypes=(("image files", "*.jpg"),("all files", "*.*")))
    			    except(OSError, FileNotFoundError):
    				    messagebox.showerror('Error','Unable to find or open file <filename>')
    			    except Exception as error:
    				    messagebox.showerror('Error','An error occurred: <error>')
        if filename:	
            self.image = cv2.imread(filename)
            self.origImage = self.image.copy()
            self.updateLabel(self.image)

    def brightness(self, option):
            if option == 'UP':
                    bias = 20
            elif option == 'DOWN':
                    bias = -20
            self.image = cv2.addWeighted(self.image, 1, np.zeros(self.image.shape, self.image.dtype), 0, bias)
            self.updateLabel(self.image)


    def contrast(self, option):
        if option == 'UP':
                gain = 1.25
        elif option == 'DOWN':
                gain = 0.8
        self.image = cv2.addWeighted(self.image, gain, np.zeros(self.image.shape, self.image.dtype), 0, 0)
        self.updateLabel(self.image)


    def revertImage(self):
                self.image = self.origImage.copy()
                self.updateLabel(self.image)

    def saveImage(self):
                try:
                        filename = filedialog.asksaveasfilename(initialdir='~/Pictures',title='Save image')
                except Exception as error:
                        messagebox.showerror('Error','An error occurred: <error>')

                if filename:
                        cv2.imwrite(filename, self.image)  

    def mythreshold(self, num1,num2):
            self.image = self.grayscale()
            self.image = cv2.threshold(self.image,num1,num2,cv2.THRESH_BINARY,self.image)
            self.updateLabel(self.image)
               
        
    def bitPlanes(self):
            pass        

    def grayscale(self):
                b = self.image[:,:,0]
                g = self.image[:,:,1]
                r = self.image[:,:,2]
                gray = 0.114*b + 0.587*g + 0.299*r
                self.image[:,:,0] = self.image[:,:,1] = self.image[:,:,2] = gray
                self.updateLabel(self.image)         
    

    
if __name__ == '__main__':
            app = Hw()
            app.mainloop()
