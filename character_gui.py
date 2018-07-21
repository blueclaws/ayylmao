##
# No longer maitained
##
from tkinter import *
from tkinter import ttk
import char
import math, time

class explorer(char.character, Frame):

    def __init__(self, master, name):
        char.character.__init__(self, name)
        #self.name = name
        self.uranium = 0
        #self.offset = 10
        self.uranium_manual = 0
        self.uranium_bonus = 0
        self.uranium_mined = 0
        #self.o2_counter = 1
        #self.oxygen = 100
        #self.start_time = time.time()
        Frame.__init__(self, master)
        self.master = master
        self.x = 0
        self.y = 0
        self.disper = StringVar()
        self.popper = StringVar()
        self.b = 0
        self.window_maker()

    def window_maker(self):
        self.master.title("Ayylmao - the game")
        self.master.geometry("400x500")

        self.b = ttk.Button(root, text = "Mine", command=self.mine)
        self.b.grid(column=0, row=0)
        self.b.columnconfigure(1, weight=1)


        #b1 = ttk.Button(root, text = "Mined", command=self.mined)
        #b1.grid(column=1, row=0)

        self.disp11 = ttk.Label(root, text="Uranium: ")
        self.popper.set(self.uranium_mined)
        self.disp11.grid(column=0, row=1, sticky=E)
        self.disp11.columnconfigure(1, weight=3)

        self.disp1 = ttk.Label(root, textvariable=self.popper)
        self.disp1.grid(column=1, row=1)

        self.disp0 = ttk.Label(root, text="Oxygen level: ")
        self.disp0.grid(column=0, row=2, sticky=E)

        self.disp01 = ttk.Label(root, textvariable=self.disper)
        self.disper.set(self.oxygen)
        self.disp01.grid(column=1, row=2)

        self.check = ttk.Checkbutton(root, text="haha")
        self.check.grid(columnspan=2)


    def mined(self):
        if self.oxygen <= 0:
            self.disper.set(" 0. YOU DIED.")
            self.b.state(['disabled'])
        else:
            self.disper.set(int(self.oxygen))

        self.popper.set(int(self.uranium_mined))


root = Tk()
app = explorer(root, 'test')
root.mainloop()
