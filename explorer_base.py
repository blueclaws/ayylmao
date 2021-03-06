####
#NO LONGER MAINTAINED
####


from char import character
import math
import time
import sys

class explorer(character):

	'''
	This is the explorer character code. Currently his abilities are as follows:
	1. Mine - uranium.
	2. Respiration.
	'''
	#constructor function
	#sets the name of the character
	#offsets the numerator for the multiplier calculation.
	#default uranium count is 0.
	#offsets the numerator for the multiplier calculation.
	#count of manual requested uranium.
	#adds the multiplier to the currently mined uranium.
	#Total life time mined uranium.
	#Offset the counter for the oxygen content.
	#max amount of oxygen player has.
	#Initialse start_time to the time when player beings the game.
	def __init__(self):
		self.uranium = 0
		self.offset = 10
		self.uranium_manual = 0
		self.uranium_bonus = 0
		self.uranium_mined = 0
		self.o2_counter = 1
		self.oxygen = 10
		self.start_time = time.time()



	def mine(self, request):
		#Offset calculation for the multiplier
		#Multiplier for the mined uranium
		#Maintains the count of all time uranium.
		#If and when the request is 1; oxygen consumed
		#is 0. This is a loophole, to fix this we send
		#request as 2 whenever player requests 1.
		if request:
			self.uranium_manual  += request
			self.offset += self.uranium_manual//100
			self.uranium_bonus = request + math.log(self.offset/10)
			self.uranium_mined += self.uranium_bonus
			self.respire(request)
			
			if self.oxygen >= 0:
				return int(self.oxygen)	
			else:
				return "You died"



	def respire(self, req):
		#intialise the 'now' to the time when this function is called
		#If the time when function is called is greater than the time when the game has started,
		#then this conditional code is executed; reduces the oxgen amount accordingly.
		#Increment the counter by one every time.
		# Prints oxygen level only when alive.

		now = time.time()

		if now > self.start_time:
				self.o2_counter += 1
				self.oxygen -= math.log(self.o2_counter)*math.log(req, 10)

			#	if self.oxygen >= 0:
					#print("Your oxygen level is: ", self.oxygen, "   ", math.log(req, 10)) Debug oxygen consumption
					#print("Your oxygen level is: ", self.oxygen)
			#		return self.oxygen
					
					




