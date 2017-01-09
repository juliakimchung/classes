from superhero import *
from flying import *
from running import *
from swimming import *
from sidekick import *
from bulletproof import*

class Superman(Bulletproof, Superhero, Flight, Running, Swimming, Sidekick ):
	def __init__ (self):
		Bulletproof.__init__(self)
		Superhero.__init__(self,"Superman", {"Flying", "Super Strength"})
	    # self.sidekicks.add(Sidekick("Jimmy Olsen"))
		self.air_speed = 1000000
		self.water_speed = 5000
		self.acceleration_rate = 3000
		self.powers.add("Bulletproof")