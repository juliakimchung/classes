class Sidekick(object):
	def __init__(self, name):
		self.name = name
		self.gender = ""
		self.alter_ego_profession = None


	def __str__ (self):
		# side_kick_output = ""
		# for sidekick in self.Sidekick():
		# 	side_kick_output += side_kick_output
		# return "{} is superhero's {}".format(self.name, side_kick_output[0: -1])

		return self.name

	def __repr__(self):
		return self.name
