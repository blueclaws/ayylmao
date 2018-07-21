import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from char import character
import math
import time 
import sys
import explorer_base as ex

class window(ex.explorer, Gtk.Window):
	
	def __init__(self):
		ex.explorer.__init__(self)
		Gtk.Window.__init__(self, title='ayylmao')

		self.canvas = Gtk.Grid()
		self.add(self.canvas)	

		self.miner = Gtk.Button(label="Mine")
		self.miner.connect("clicked", self.mine_signal)
		self.canvas.attach(self.miner, 0, 0, 3, 1)
		
		self.oxygen_label = Gtk.Label()
		self.oxygen_label.set_text("Oxygen level: ")
		self.canvas.attach(self.oxygen_label, 0, 2, 1, 1)
		
		self.oxygen_disp = Gtk.Label()
		self.oxygen_disp.set_text(str(self.oxygen))
		self.canvas.attach(self.oxygen_disp, 1, 2, 1, 1)

		self.mine_label = Gtk.Label()
		self.mine_label.set_text("Uranium level: ")
		self.canvas.attach(self.mine_label, 0, 3, 1, 1)
		
		self.mine_disp = Gtk.Label()
		self.mine_disp.set_text(str(self.uranium_mined))
		self.canvas.attach(self.mine_disp, 1, 3, 1, 1)

		
	def mine_signal(self, widget):
		if self.oxygen >= 0:
			self.oxygen_disp.set_text(str(ex.explorer.mine(self, 2)))
			self.mine_disp.set_text(str(self.uranium_mined))
	

win = window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()	
