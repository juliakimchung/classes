from superman import *

# if __name__ == "__main__":
jimmy_olsen = Sidekick("Jimmy Olsen")
Sidekick.gender = "female"
superman = Superman()
superman.sidekicks.add(jimmy_olsen)

superman.add_powers("X-Ray vision")
superman.add_powers("Invisibility")
print(superman)
superman.fly()
superman.swim()
superman.run()
print(dir(Sidekick))
print(superman.sidekicks)