import datetime

class Error(Exception):
	'''Base class for other exceptions'''
	pass
class TooLong(Error):
	"""Raised when input value not M or F"""
	pass
class TooShort(Error):
	"""Raised when input value not M or F"""
	pass
class InvalidEntry(Error):
	"""Raised when input value not M or F"""
	pass
class ValueNotGender(Error):
	"""Raised when input value not M or F"""
	pass
class StrError(Error):
	"""Raised when input value not M or F"""
	pass

class database:
	def __init__(self): # initialises a list to store students in
		self.allstudents = [] 
	def add_student(self, student): # a function for appending the list of students
		self.allstudents.append(student)
	def sizeof(self): # a function for returning the size of the list
		return len(self.allstudents)
	def get(self): # function for returning the list of students 
		return self.allstudents

class Student:
	''' A student class with two properties all students will have nomatter their other properties'''
	course='Science'
	lecturer='Nill Bye the Science Guy'
	def __init__(self,inp_name, inp_lastname,inp_address,inp_dob,inp_gender): # when you initialise a new student give them a name, last name...etc.
		self.name=inp_name
		self.lastname=inp_lastname
		self.address=inp_address
		self.dob=inp_dob
		self.gender=inp_gender
	def editfirstname(self, newname): # functions for editing details, you don't need these.
		self.name=newname
	def editsecondname(self, newname):
		self.lastname=newname
	def editaddress(self, newadd):
		self.address=newadd
	def editdob(self,newdob):
		self.dob=newdob
	def editgender(self,newgender):
		self.gender=newgender
	def returndetails(self): # function for returning details 
		print('First Name: ', self.name, ' Surname: ', self.lastname,' Address: ', self.address,' D.O.B.: ', self.dob,' Gender: ', self.gender)

def nameentry(nametype):
	'''user input for the name with validation'''
	while True:
		try:
			inp_aname=str(input('\n Enter ' + str(nametype) + ' name: '))
			if len(inp_aname)>20:
				raise TooLong
			elif len(inp_aname)<=1:
				raise TooShort 
			elif all(x.isalpha() or x.isspace() for x in inp_aname) is False: # this says if it isn't true that all of the elements of inp_aname are either a letter or a space then raise an error
				raise StrError
			else:
				break
		except StrError:
			print("\n Please enter a valid name: ")
		except TooLong:
			print("\n Name entered is too long, please retry: ")
		except TooShort:
			print("\n Name entered is too short, please retry: ")
	return inp_aname

def addressentry():
	'''user input for the address with validation'''
	while True:
		try:
			inp_number=int(input("\n Enter street number: "))
			if inp_number<=0:
				raise InvalidEntry
			elif inp_number>9999:
				raise InvalidEntry
			else:
				break
		except InvalidEntry:
			print("\n Please enter a valid street number: ")
		except ValueError:
			print("\n Please enter a valid street number: ")
	while True:
		try:
			inp_street=str(input("\n Enter street name (no spaces): "))
			if len(inp_street)>50:
				raise TooLong
			elif len(inp_street)<=1:
				raise TooShort 
			elif all(x.isalpha() or x.isspace() for x in inp_street) is False:
				raise StrError
			else:
				break
		except StrError:
			print("\n Please enter a valid address: ")
		except TooLong:
			print("\n Address entered is too long, please retry: ")
		except TooShort:
			print("\n Address entered is too short, please retry: ")
	return str(str(inp_number) + ' ' + inp_street)

def dobentry():
	'''user input for  dob with validation'''
	isValid=False
	while not isValid:
		userIn = input("\n Type DOB (dd/mm/yyyy): ")
		try: 
			inp_dob = datetime.datetime.strptime(userIn, "%d/%M/%Y")
			isValid=True
		except:
			print("\n Please try again. Type Date in (dd/mm/yyyy) format: ")
	inp_dob=str(inp_dob.day)+'/'+ str(inp_dob.month) +'/'+ str(inp_dob.year)
	return inp_dob

def genderentry():
	'''user input for gender with validation'''
	while True:
		try:
			inp_gender=str(input('\n Enter gender (M for male, F for female, or X for other) here:'))
			if ((inp_gender!='M') and (inp_gender!='F') and (inp_gender!='X')):
				raise ValueNotGender
			else:
				break
		except ValueNotGender:
			print("\n Please enter either M for male, F for female or X for other: ")
	return inp_gender

def createstudent():
	nametype='first'
	a = nameentry(nametype) # first name user input
	nametype='last'
	b=nameentry(nametype) # second name user input
	c=addressentry() # address user input
	d=dobentry() # dob user input
	e=genderentry() # gender user input
	studentcreation=Student(a,b,c,d,e) # create a student object with these values 
	return studentcreation

def accessstudentdata(studentdatabase): # function for searching for students and outputting their info
	'''Function for searching for students records'''
	while True:
		try:
			search_secondname=str(input("\n Surname to search: "))
			if len(search_secondname)>20:
				raise TooLong
			elif len(search_secondname)<=1:
				raise TooShort 
			if all(x.isalpha() or x.isspace() for x in search_secondname) is False:
				raise StrError
			else:
				break
		except StrError:
			print("\n Please enter a valid name.")
		except TooLong:
			print("\n Address entered is too long, please retry: ")
		except TooShort:
			print("\n Address entered is too short, please retry: ")
	searched_student=[]
	student_name_details=[]
	for i in range(0, studentdatabase.sizeof()):
		student_name_details.append(studentdatabase.get()[0].lastname)
	if search_secondname in student_name_details:
		index=student_name_details.index(search_secondname)
		studentdatabase.get()[index].returndetails()
	elif search_secondname not in student_name_details:
		print('\n Student not found.')

def percentages(studentdatabase): # calculating percentage breakdown
	genderlist=[]
	for i in range(0,studentdatabase.sizeof()):
		genderlist.append(studentdatabase.get()[i].gender)
	male=genderlist.count('M')
	female=genderlist.count('F')
	other=genderlist.count('X')
	total=male+female+other 
	male_perc=round(100*male/total)
	female_perc=round(100*female/total)
	other_perc=round(100*other/total)
	return male_perc,female_perc,other_perc

def optionsmenu(student_database):
	'''A user input menu screen'''
	print('\n  ------ Welcome to the student data base  ------  \n')
	print(' 1. Print student records.')
	print(' 2. Add new student.')
	print(' 3. Search student records by last name.')
	print(' 4. Percentages. \n' )
	while True:
		try:
			user_selection=int(input("\n Choose a menu option by selecting a number: "))
			break
		except ValueError:
			print("\n Choose a valid menu option by selecting a number: ")
	if user_selection==1:
		if student_database.sizeof()>0: # if there's more than one entry ...
			for i in range(0,student_database.sizeof()): # ... use the returndetails() function to print them
				student_database.get()[i].returndetails()
		else:
			return print('\n No student data available.') # ... otherwise return this
	elif user_selection==2:
		newperson=createstudent() # use the createstudent() function to make a new student using the input functions
		student_database.add_student(newperson) # use the add_student function to append the list of students in the database
	elif user_selection==3:
		searchname=accessstudentdata(student_database)
	elif user_selection==4:
		male,female,other = percentages(student_database)
		print('Percent Male: ', male, 'Percent Female: ', female, 'Percent Other: ', other)

def main():
	student_database=database()
	while True:
		optionsmenu(student_database)

if __name__=='__main__':
	main()
