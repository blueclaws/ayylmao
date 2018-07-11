from char import character
import math

class explorer(character):
	
	''' 
	This is the explorer character code. Currently his abilities are as follows:
	1. Mine - uranium.
	'''

	def __init__(self, name):				#constructor function
		self.name = name				#sets the name of the character
		self.offset = 10				#offsets the numerator for the multiplier calculation.
		self.uranium = 0				#default uranium count is 0.
		self.uranium_manual = 0				#count of manual requested uranium.
		self.uranium_bonus = 0				#adds the multiplier to the currently mined uranium.
		self.uranium_mined = 0				#Total life time mined uranium.
		
	
	
	def mine(self, request):
		
		if request:
			self.uranium_manual  += request						#Stores the amount of uranium requested by the player(all time).
			self.offset += self.uranium_manual//100					#Offset calculation for the multiplier
			self.uranium_bonus = request + math.log(self.offset/10)			#Multiplier for the mined uranium.
			self.uranium_mined += self.uranium_bonus				#Maintains the count of all time uranium.
			return self.uranium_mined						
	
	def mined(self):
		print("You have mined a total of", self.uranium_mined, "uranium")		#Prints total uranium mined ever.
	

#testing the module~~
player = explorer('test')
while True:
	z = 0
	y = int(input("How much: "))
	player.mine(y)
	player.mined()
