from tkinter import *
import sys, time

class Window(Frame):

        def __init__(self, master):
                Frame.__init__(self, master)
                self.master = master
                self.window_maker()

        def window_maker(self):
                self.master.title("Test gui")
                self.pack(fill=BOTH, expand=1)
                exit_button = Button(self, text="Quit", command=self.exit_me)
                exit_button.place(x=0, y=0)


        def exit_me(self):
                sys.exit()



root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()
