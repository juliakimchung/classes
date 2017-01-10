import unittest
from superman import *
class TestSuperman(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		print("set up class")
		self.superman = Superman()

	def test_SupermanIsBulletproof(self):
		
		self.assertIsInstance(self.superman, Bulletproof)

	def test_SupermanhasFlyMethod(self):
		# superman = Superman()
		self.assertIn('fly', dir(self.superman))

	def test_SupermanIsSwimmingFast(self):
		# superman = Superman()
		self.assertEqual(self.superman.water_speed, 5000)

	def test_SupermanIsFlyingFast(self):
		# superman = Superman()
		self.assertEqual(self.superman.air_speed, 1000000)

	def test_SupermanIsASuperhero(self):
		# superman = Superman()
		self.assertIsInstance(self.superman, Superhero)
		# assertIsInstance(obj, class)

	def test_SupermanIsAFlyingSuperhero(self):

		# superman = Superman()
		self.assertIsInstance(self.superman, Flight)

	def test_SupermanIsARunningSuperhero(self):
		# superman = Superman()
		self.assertIsInstance(self.superman, Running)

	def test_SupermanIsASwimmingSuperhero(self):
		# superman = Superman()
		self.assertIsInstance(self.superman, Swimming)
	
if __name__ == '__main__':
		unittest.main()
