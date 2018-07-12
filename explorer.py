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

	def __init__(self, name):				#constructor function
		self.name = name				#sets the name of the character
		self.offset = 10				#offsets the numerator for the multiplier calculation.
		self.uranium = 0				#default uranium count is 0.
		self.uranium_manual = 0				#count of manual requested uranium.
		self.uranium_bonus = 0				#adds the multiplier to the currently mined uranium.
		self.uranium_mined = 0				#Total life time mined uranium.
		self.o2_counter = 1				#Offset the counter for the oxygen content.
		self.oxygen = 10				#max amount of oxygen player has.
		self.start_time = time.time()			#Initialse start_time to the time when player beings the game.


	def mine(self, request):

		if request:
			self.uranium_manual  += request									#Stores the amount of uranium requested by the player(all time).
			self.offset += self.uranium_manual//100							#Offset calculation for the multiplier
			self.uranium_bonus = request + math.log(self.offset/10)			#Multiplier for the mined uranium.
			self.uranium_mined += self.uranium_bonus						#Maintains the count of all time uranium.
			if request > 1:													#If and when the request is 1; oxygen consumed
				self.respire(request)										#is 0. This is a loophole, to fix this we send
			else:															#request as 2 whenever player requests 1.
				self.respire(2)


			if self.oxygen <= 0:							# If oxygen level is 0; you die.
				print("Oxygen reached 0. YOU DIED.")
				time.sleep(3)								#waits X seconds before exiting the game
				sys.exit()									#Exit the script
			return self.uranium_mined

	def respire(self, req):
		now = time.time()													#intialise the 'now' to the time when this function is called

		if now > self.start_time:											#If the time when function is called is greater than the time when the game has started,
				self.oxygen -= math.log(self.o2_counter)*math.log(req, 10)	#then this conditional code is executed; reduces the oxgen amount accordingly.
				self.o2_counter += 1										#Increment the counter by one every time.

				if self.oxygen >= 0:										# Prints oxygen level only when alive.
					#print("Your oxygen level is: ", self.oxygen, "   ", math.log(req, 10)) Debug oxygen consumption
					print("Your oxygen level is: ", self.oxygen)



	def mined(self):
		if self.oxygen > 0:															#Only when alive.
			print("You have mined a total of", self.uranium_mined, "uranium")		#Prints total uranium mined ever.


#testing the module~~
player = explorer('test')
while True:
	z = 0
	y = int(input("How much: "))
	player.mine(y)
	player.mined()
