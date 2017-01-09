class Company(object):
	"""This represents a company in which people work"""

	def __init__(self):
		self.name = ""
		self.address = ""

		self.employee = set()

		# Employee.__init__(self, name, job_title, start_day)

	# def __repr__ (self):
	# 	return self.name
	# def getName(self):

	# 	def __str__(self):
	# 		return self.name
	# 	def __repr__(self):
	# 		return self.name
	# def getTitle(self):
	# 	return self.title

	# def getStart_date(self):
	# 	return self.start_date

class Employee:
	def __init__ (self, name, job_title, start_day):
		self.name = name
		self.job_title = job_title
		self.start_day = start_day


	def __repr__ (self):
		return "{0}, {1}, {2}".format(self.name, self.job_title, self.start_day)

if __name__ == '__main__':

	company = Company()

	Julia = Employee("Julia Kim_Chung", "software developer", "04-01-17")
	Randy = Employee("Randy Taylor", "project manager", "10-10-10")
	Madison = Employee("Madison Princess", "CEO", "10-17-2006")



	company.employee.add(Julia)
	company.employee.add(Randy)
	company.employee.add(Madison)
	print(Julia)
	print(Madison)
	print(company.employee)


# print(company.getName(AI))
# print(company)
# print(company.employees.add(Julia))

