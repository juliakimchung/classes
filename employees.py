class Company(object):
	"""This represents a company in which people work"""

	def __init__(self, name, address, history):
		self.name = name
		self.address = address
		self.history = history

		self.employee = set()

class Employee:
	def __init__ (self, name, job_title, start_day, company_name):
		self.name = name
		self.job_title = job_title
		self.start_day = start_day
		self.company_name = company_name


	def __repr__ (self):
		return "{0}, {1}, {2}, {3}".format(self.name, self.job_title, self.start_day, self.company_name)

if __name__ == '__main__':

	company = Company("Apple", "1111 Apple st NY, NY", "40 years old")

	Julia = Employee("Julia Kim_Chung", "software engineer", "04-01-17", "Eventbrite")
	Randy = Employee("Randy Taylor", "project manager", "10-10-10", "facebook")
	Madison = Employee("Madison Princess", "CEO", "10-17-2006","Harvard" )

	David = Employee("David King", "President", "1-1-2017", "Vanderbilt")


	company.employee.add(Julia)
	company.employee.add(Randy)
	company.employee.remove(Randy)
	company.employee.add(Madison)
	print(Julia)
	print(Madison)
	print(company.employee)

	new_company = Company("Eventbrite", "111 Brite St Nashville, TN", "3 years old")

	new_company.employee.add(Randy)
	new_company.employee.add(David)
	print(dir(new_company))
	print(new_company.employee)
	new_company.name = "facebook"
	print(new_company.name)
	print(new_company.name + " is located in " + new_company.address )
	print(David)
	print(new_company.address)

	another_company = Company("Harvard", "1111 Boston MA", "100 years old")
	print(another_company.history)
	another_company.employee.add("Madison")
	print(another_company.employee)
	print(Madison)


