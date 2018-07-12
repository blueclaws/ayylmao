from tkinter import *

class Window(Frame):

        def __init__(self, master):
                Frame.__init__(self, master)
                self.master = master
                self.window_maker()

        def window_maker(self):
                self.master.title("Test gui")
                self.pack(fill=BOTH, expand=1)


root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()
