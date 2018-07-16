'''
This is character code.

'''
import time
import math
class character:

	def __init__(self, name):
		self.name = name
		self.offset = 10
		self.o2_counter = 1
		self.oxygen = 100
		self.start_time = time.time()

	def respire(self, req):

		now = time.time()

		if now > self.start_time:
			self.o2_counter += 1
			self.oxygen -= math.log(self.o2_counter)*math.log(req, 10)

			if self.oxygen >= 0:
				return self.oxygen

	def mine(self):
		 self.uranium_manual  += 1
		 self.offset += self.uranium_manual//50
		 self.uranium_bonus = 1 + math.log(self.offset/10)
		 self.uranium_mined += self.uranium_bonus
		 y = self.respire(2)
		 x = self.uranium_mined
		 self.mined()
