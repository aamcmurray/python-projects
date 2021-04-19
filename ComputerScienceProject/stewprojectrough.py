import datetime 

class Error(Exception):
	"""Base class for other exceptions"""
	pass
class ValueNotGender(Error):
	"""Raised when input value not M or F"""
	pass

def studentinput():
	'''Function for assigning variables to new student details'''
	while True:
		try:
			inp_firstname=str(input("\n Enter firstname here: "))
			inp_secondname=str(input("\n Enter second name here: "))
			break
		except ValueError:
			print("\n Please enter a valid name: ")
	while True:
		try:
			inp_gender=str(input('\n Enter gender (M/F) here:')) # I was lazy so there's only two genders here atm, you can expand easily. 
			if ((inp_gender!='M') and (inp_gender!='F')):
				raise ValueNotGender
			else:
				break
		except ValueNotGender:
			print("\n Please enter either M or F: ")
	return inp_firstname,inp_secondname,inp_gender

def studentinputdob(): # I did dob separately because the code was a bit messy but ideally you would keep all the input together
	'''function for assigning a variable to new student dob'''
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

def addstudent(studentdetails):
	'''Function for inputting the new student variables into the database & returning the new version'''
	inp_firstname,inp_secondname,inp_gender=studentinput()
	inp_dob=studentinputdob()
	studentdetails['names'].append(inp_firstname)
	studentdetails['secondnames'].append(inp_secondname)
	studentdetails['dobs'].append(inp_dob)
	studentdetails['gender'].append(inp_gender)
	return studentdetails

def accessstudentdata(studentdetails):
	'''Function for searching for students records'''
	while True:
		try:
			search_secondname=str(input("\n Search second name: "))
			break
		except ValueError:
			print("\n Please enter valid name.")
	return search_secondname

def searcher(search_secondname,studentdetails):
	searched_student=[] # initialise a list to hold the details of the student if they're found
	if search_secondname in studentdetails['secondnames']: # if the user input search term is in the data base then...
		index=studentdetails['secondnames'].index(search_secondname) #... give me the index of where that search term is in the data base
		for j in range(0,4): # ugly one liner for loop that just grabs the student's data using the index. 
			searched_student.append([studentdetails.get(k) for k in ['names', 'secondnames','dobs','gender']][j][index])	
		print('\n Name: ', searched_student[0]+' '+ searched_student[1])
		print(' D.O.B.: ', searched_student[2])
		print(' Gender: ', searched_student[3], '\n')
	elif search_secondname not in studentdetails['secondnames']:
		print('\n Student not found.')

def optionsmenu(studentdetails):
	'''A user input menu screen'''
	print('\n  ------ Welcome to the student data base  ------  \n')
	print(' 1. Print student records.')
	print(' 2. Add new student.')
	print(' 3. Search student records by last name. \n')
	while True: # validation for the menu input 
		try:
			user_selection=int(input("\n Choose a menu option by selecting a number: "))
			break
		except ValueError:
			print("\n Choose a valid menu option by selecting a number: ")
	if user_selection==1:
		print('\n ------ Student Database ------ \n')
		duplicate=studentdetails.copy() # makes a duplicate of the data base so i can just use the pop() functionality of dictionaries to easily get the values, not the best way to do things but alright for a project like this.
		names=duplicate.pop('names')
		secondnames=duplicate.pop('secondnames')
		dobs=duplicate.pop('dobs')
		genders=duplicate.pop('gender')
		for i in range(0,len (names)): # just prints whatever i got from the pop()s above
			print(' Name: ', names[i]+' '+ secondnames[i])
			print(' D.O.B.: ', dobs[i])
			print(' Gender: ', genders[i], '\n')
	elif user_selection==2:
		addstudent(studentdetails) # run the add student function
	elif user_selection==3:
		search_secondname=accessstudentdata(studentdetails) # run the search function
		searcher(search_secondname,studentdetails) #

def main():
	studentdetails={'names':[], 'secondnames':[],'dobs':[], 'gender':[]} # make a dictionary with some keys and empty lists to be filled when adding students details
  # there's better ways to do this but this will work fine. like 
  # make a list of all the students: allstudents=[]
  # make a dictionary for each student: student= {'name': 'jim', 'secondname':'jimmerson'}
  # add that dictionary to the list as you go: allstudents.append(student)
  # retreive it with allstudents[0] or allstudents[1]...etc.
  # that would be a bit cleaner, but i was sorta just seat of the pants coding and not planning so you got the less good version. 
	while True:
		optionsmenu(studentdetails) # go to the options menu in an infinite loop

if __name__=='__main__':
	main()
