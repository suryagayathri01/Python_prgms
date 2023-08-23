from breezypythongui import EasyFrame
class mynewgui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="taskbar",height=150,width=250)
        self.text=self.addLabel(text="welcome guys",row=0,column=0)
        self.addButton(text="clickme",row=1,column=0,command=self.on_button_click)
        self.clearBtn=self.addButton(text="clear",row=2,column=1,command=self.clear)
        self.restoreBtn=self.addButton(text="restore",row=2,column=0,command=self.restore)
    def on_button_click(self):
        self.text["text"]="button clicked!!"
    def clear(self):
        clearBtn["state"]="disabled"
        restoreBtn["state"]="normal"
    def restore(self):
        clearBtn["state"]="normal"
        restoreBtn["state"]="disabled"
if __name__=="__main__":
    mynewgui().mainloop()


