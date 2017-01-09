class Running(object):
	def __init__(self):
		self.ground_speed = 0
		self.acceleration_rate = 0

	def run(self):
		print("I can run at {}".format(self.acceleration_rate))