#import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

#exception handling
class Error(Exception):
	"""Base class for other exceptions"""
	pass
class ValueTooSmallError(Error):
	"""Raised when input value too small"""
	pass
class ValueTooLargeError(Error):
	"""Raised when input value too large"""
	pass
class ValueNotAcceptedError(Error):
	"""Raised when input value not in range"""
	pass

#user input functions 
def userinput():
	while True:
		try:
			inputval=int(input(" Enter number here: "))
			if inputval <0:
				raise ValueTooSmallError
			elif inputval > 12:
				raise ValueTooLargeError
			break
		except ValueTooSmallError:
			print(" Please enter a number.")
		except ValueTooLargeError:
			print(" Please enter a number.")
		except ValueError:
			print(" Please enter a number.")
	return inputval

def bookinput():
	while True:
		try:
			book_details=str(input("Enter details here: "))
			break
		except ValueError:
			print("Enter details: ")
	return book_details

def bookinputtwo():
	while True:
		try:
			book_details=int(input("Enter details here: "))
			break
		except ValueError:
			print("Enter details: ")
	return book_details

#for reading data in from a text file
def reader(path):
	b=[]
	f = open(path, 'r', encoding='utf-8-sig') # opens the text file. specifying the encoding ensures no strange characters appear.
	next(f) # skips the first line since it's just details
	conts=f.readline().rstrip().replace('#', ' ').split(',') #reads the line, rstrip removes '\n's, replace substitutes '#'s for spaces, split separates the line anywhere a comma appears.
	for line in f: # for loop going from the first unread line in the text file to the last
		text=line.rstrip().split(',') # just splitting the line that's being read up and saving it as a variable
		book_details={conts[i]:text[i] for i in range(0,len(conts))} # a dictionary comprehension builds dictionaries from key and value expressions, here i've set the keys to be each item in contents (i.e., author, title...etc) and the values are being pulled from the text line we're reading right now, i.e., (P.G.Woodhouse, Right Ho Jeeves,...etc)
		b.append(book_details)
	return b, conts

# a main display providing options to the user
def options_display(c):
	print(' Select listing to be displayed, in alpha-numeric order, by entering a real number between 0 and ', len(c)-1, '. \n','Alternatively press ', len(c), 'to display the details of all titles. \n', 'Finally, press 9 for stock analysis')
	counter=0
	for i in range(0,len(c)):
		print(i, c[i])
		counter+=1
	print(counter, ' DETAILS OF ALL TITLES')
	print(8, ' EXIT')
	print(9, ' STOCK ANALYSIS')
	print(10, ' DETAILS ON AVAILABLE GENRES')
	print(11, 'ADD NEW ENTRY')
	print(12, 'AVAILABILITY')

# a function that determines what happens given different user inputs on the main menu
def choices(inp_v,b,c):
	if inp_v<7:
		# i'm initialising a set and a list, when you use .add on a list it will add an entry, provided its not already in the set, this is useful for things like titles and authors but not good for cost and stock
		contents_set=set() # for authors, titles, formats, publishers, genre
		contents_list=[] # for cost and stock
		for i in range(0, len(c)):
			if inp_v==i:
				print(' List of', str(c[i]))
				if inp_v!=4 and inp_v!=5:
					for j in range(0, len(b)):
						contents_set.add(b[j][c[i]])
					print('Alphabetical order: ', sorted(contents_set))
					#for i in range(0,len(contents_set)):
					#	print(' - ', contents_set.pop())
				else:
					for j in range(0,len(b)):
						contents_list.append(b[j][c[i]])
					print('Numeric order: ', sorted(contents_list))
					#for i in range(0,len(contents_list)):
					#	print(' - ', contents_list[i])
	elif inp_v==7:
		for i in range(0, len(b)):
			print(' - ', b[i][c[1]])
			for k, v in b[i].items():
				print(k, v)
	elif inp_v==8:
		quit()
	elif inp_v==9:
		stockanalysis(b,c)
	elif inp_v==10:
		genretotals(b,c)
	elif inp_v==11:
		previous=averagecost(b,c)
		b=addnewbook(b,c)
		new=averagecost(b,c)
		print('Previous average cost: ',previous,'New average cost: ', new)
		print('Difference in averages: ', round((int(new)-int(previous)),2))
	elif inp_v==12:
		availability(b,c)
#performs analysis of the stock, calculating the total stock value and the average price of available books
def stockanalysis(b,c):
	print(' Title - Stock - Value (£) ')#
	value=0
	for i in range(0, len(b)):
		val=round(float(b[i][c[5]])*float(b[i][c[4]]),2)
		print(b[i][c[1]],' - ', b[i][c[5]], ' - ', val)
		value+=val
	print(' Total stock value: £',value)
	av=averagecost(b,c)
	print(' Average price of books in stock: £', av)
	
# calculates the average cost of available books
def averagecost(b,c):
	prices=[]
	for i in range(0, len(b)):
		prices.append(float((b[i][c[4]].replace(' ',''))))
	#find the position of any books with 0 stock and record it in a list
	no_stock_index=[]
	for i in range(0,len(b)):
		stock=int(b[i][c[5]])
		if stock==0:
			no_stock_index.append(i)
		else: 
			continue
	for i in range(0, len(no_stock_index)):
		del prices[no_stock_index[i]]
	average=round(sum(prices)/len(prices),2)
	return average

# returns the available unique genres
def genretotals(b,c):
	unique_genres=set()
	for i in range(0, len(b)):
		genres=b[i][c[6]]
		if genres in unique_genres:
			continue
		elif genres not in unique_genres:
			unique_genres.add(genres)
	print(" There are :", len(unique_genres), " unique genres in stock.")
	genreadd(b,c,unique_genres)
# plots genre against total books of that genre
def genreadd(b,c,ug):
	genre_sum=0
	genre_list=[]
	x=[]
	y=[]
	for i in range(0,len(ug)):
		check_genre=ug.pop()
		counter=0
		for i in range(0,len(b)):
			if check_genre==b[i][c[6]]:
				genre_sum+=int(b[i][c[5]])
				counter+=1
		print(" There are ", genre_sum, "books of ", check_genre, " including duplicates.")
		x.append(str(check_genre))
		y.append(genre_sum)
		print(" There are ", counter, "unique books of ", check_genre)
	plt.bar(x,y)
	plt.show()

# function allowing a user to add a new book entry
def addnewbook(b,c):
	textin_list=[]
	for i in range(0,7):
		if i <4:
			print('Please enter string to describe the : ', c[i])
			textin_list.append(bookinput())
		if 4<=i<=5:
			print('Please enter numeric value to describe the : ', c[i])
			textin_list.append(str(bookinputtwo()))
		if i==6:
			print('Please enter string to describe the : ', c[i])
			textin_list.append(bookinput())
	book_details={c[i]:textin_list[i] for i in range(0,len(c))}
	#print(book_details)
	total_stocked=0
	for i in range(0, len(b)):
		total_stocked+=int(b[i][c[5]])
	print('stock was: ', total_stocked)
	b.append(book_details)
	total_stocked=0
	for i in range(0, len(b)):
		total_stocked+=int(b[i][c[5]])
	print('stock now: ', total_stocked)
	return b

#function allowing user to check availability of a book
def availability(b,c):
	print('Check if a title is listed in the database by typing the title below.')
	named_book=str(' ')+str(bookinput())
	books_available=set()
	for i in range(0, len(b)):
		books_available.add(b[i][c[1]])
	print(named_book, books_available)
	if named_book in books_available:
		print(named_book, 'is listed')
		for i in range(0,len(b)):
			if named_book==b[i][c[1]]:
				print('stock level: ', b[i][c[5]])
			else:
				continue
	else:
		print(named_book, 'is not listed')
		print('stock level:', 0)
# the main loop that calls everything
def main():
	path='C:/Users/User/Place/bookstocks.txt'
	bank, contents=reader(path)
	while True: 
		options_display(contents)
		choice=userinput()
		choices(choice,bank,contents)

if __name__=='__main__':
	main()
