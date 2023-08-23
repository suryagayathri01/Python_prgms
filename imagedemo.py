from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class Imagedemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="smokeypic",height=500,width=300)
        self.setResizable(False)
        imagelabel=self.addLabel(text="",row=0,column=0)
        textlabel=self.addLabel(text="smokey cat",row=1,column=0)
        self.image=PhotoImage("C:/Users/SURYAGAYATHRI/Desktop/Cpro/PYTHON/smokey.gif")
        imagelabel["image"]=self.image
        textlabel["foreground"]="blue"
if __name__=="__main__":
    Imagedemo().mainloop()

