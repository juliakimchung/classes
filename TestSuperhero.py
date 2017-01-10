import unittest
from superhero import *
class TestSuperhero(unittest.TestCase):

	def test_SuperheroMustHaveNameProperty(self):

		random_superhero = Superhero("Bilbo")
		self.assertEqual(random_superhero.name, "Bilbo")

	def test_SuperheroAddPowerMustIncludePower(self):

		random_superhero = Superhero("Clark")
		random_superhero.add_powers("Invisibility")
		self.assertIn("Invisibility", random_superhero.powers)

	def test_SuperheroRemovePowerMustIncludePower(self):

		random_superhero = Superhero("Clark")
		random_superhero.add_powers("Invisibility")
		random_superhero.remove_powers("Invisibility")
		self.assertNotIn("Invisibility", random_superhero.powers)

if __name__ == '__main__':
		unittest.main()
