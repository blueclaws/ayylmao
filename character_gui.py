from tkinter import *
from tkinter import ttk
from char import character
import math, time

class explorer(character, Frame):

    def __init__(self, master, name):
        self.name = name
        self.uranium = 0
        self.offset = 10
        self.uranium_manual = 0
        self.uranium_bonus = 0
        self.uranium_mined = 0
        self.o2_counter = 1
        self.oxygen = 10
        self.start_time = time.time()
        Frame.__init__(self, master)
        self.master = master
        self.x = 0
        self.y = 0
        self.disper = StringVar()
        self.popper = StringVar()
        self.window_maker()

    def window_maker(self):
        self.master.title("Ayylmao - the game")
        self.master.geometry("400x500")

        b = ttk.Button(root, text = "Mine", command=self.mine)
        b.grid(column=0, row=0)

        b1 = ttk.Button(root, text = "Mined", command=self.mined)
        b1.grid(column=1, row=0)

        disp = ttk.Label(root, textvariable=self.disper)
        disp.grid(column=1, row=2)

        disp1 = ttk.Label(root, textvariable=self.popper)
        disp1.grid(column=1, row=1)

    def mine(self):
        self.uranium_manual  += 1
        self.offset += self.uranium_manual//100
        self.uranium_bonus = 1 + math.log(self.offset/10)
        self.uranium_mined += self.uranium_bonus
        y = self.respire(2)
        #if self.oxygen <= 0:
            #print("Oxygen reached 0. YOU DIED.")
            #>>>>>>>>>>>>>>self.disper.set("OwO")
        #return self.uranium_mined
        x = self.uranium_mined

    def respire(self, req):

        now = time.time()

        if now > self.start_time:
            self.oxygen -= math.log(self.o2_counter)*math.log(req, 10)
            self.o2_counter += 1

            if self.oxygen >= 0:
                return self.oxygen

    def mined(self):
        if self.oxygen <= 0:
            self.disper.set("Oxygen reached 0. YOU DIED.")

        self.popper.set(self.uranium_mined)


root = Tk()
app = explorer(root, 'test')
root.mainloop()
