
class Superhero(object):

	def __init__(self, name):
		self.powers = set()
		self.name = name
		self.gender = ''
		self.super_friends = set()
		self.evil_enemies = set()
		self.sidekicks = set()
		self.weakness = set()
		self.lair = ""
		self.biological_parents = tuple()


	def fight(self):
		pass

	def get_powers(self):
		return self.powers

	def add_powers(self, new_powers):
		self.powers.add(new_powers)

	def remove_powers(self, power_to_remove):
		self.powers.remove(power_to_remove)

	def __str__(self):
		power_output = ""
		for power in self.get_powers():
			power_output += power + ", "
		return "{} superhero with powers:{}".format(self.name, power_output[0:-2])


# jimmy_olsen = Sidekick("Jimmy Olsen")
# Sidekick.gender = "female"
# superman = Superman()
# superman.sidekicks.add(jimmy_olsen)

# superman.add_powers("X-Ray vision")
# superman.add_powers("Invisibility")
# print(superman)
# superman.fly()
# superman.swim()
# superman.run()
# print(dir(Sidekick))
# print(superman.sidekicks)
# print (dir(superman))

