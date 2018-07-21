from tkinter import *
from tkinter import ttk

class Window(Frame):

        def __init__(self, master):
                Frame.__init__(self, master)
                self.master = master
                self.disper = StringVar()
                self.username = StringVar()
                self.window_maker()

        def WoopDeDoo(self):
                self.disper.set("OwO")

        def window_maker(self):
                self.master.title("Ayylmao - The game.")
                self.master.geometry("400x500")


                b = ttk.Button(root, text="Mine", command=self.WoopDeDoo)
                b.grid(column=0, row=0)



                #name = ttk.Entry(root, textvariable=self.username)
                #name.grid(column=1, row=0)


                disp = ttk.Label(root, text="xxxx", textvariable=self.disper)
                disp.grid(column=1, row=0)





root = Tk()
app = Window(root)
#root.bind('<Return>', calculate)
root.mainloop()
