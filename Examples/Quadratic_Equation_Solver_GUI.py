import sys
from PyQt5 import QtWidgets as qtw #  Includes your widgets 
from PyQt5 import QtCore as qtc #  Lower level stuff, like signals and slots
from PyQt5 import QtGui as qtg #  Contains classes that aren't widgets but are related to the gui such as fonts and color classes
import math as math
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt 
import random 
import numpy as np

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs): #  Double underscore methods are called dunder methods. They're special. The init is what gets called when we create an instance of a class. self refers to the instance of the object we're creating
		super().__init__(*args, **kwargs) # super() gives us a reference to our parent object (here it's the qwidget object) and here we're calling the init method for it and pass the arguments 
		self.coefficient_a=qtw.QLineEdit() # use self. so we can reference this when outsite the init method
		self.coefficient_b=qtw.QLineEdit()
		self.coefficient_c=qtw.QLineEdit()
		self.result=qtw.QLineEdit()
		self.title=qtw.QLabel('Quadratic Equation Solver')
		self.title.setAlignment(qtc.Qt.AlignCenter)
		self.descriptive=qtw.QLabel('Enter the coefficients of a quadratic equation (of the form ax^2+bx+c=0) and press submit to solve for x.')
		self.descriptive.setAlignment(qtc.Qt.AlignCenter)
		self.cancel_button=qtw.QPushButton('Quit')
		self.submit_button=qtw.QPushButton('Submit')
		self.figure=plt.figure()
		self.canvas=FigureCanvas(self.figure)
		self.toolbar=NavigationToolbar(self.canvas, self)
		self.button=qtw.QPushButton('Plot')
		self.button.clicked.connect(self.plot)
		layout = qtw.QFormLayout()
		layout.addRow(self.title)
		layout.addRow(self.descriptive)
		layout.addRow('Coefficient a: ', self.coefficient_a)
		layout.addRow('Coefficient b: ', self.coefficient_b)
		layout.addRow('Coefficient c: ', self.coefficient_c)
		button_widget=qtw.QWidget()
		button_widget.setLayout(qtw.QHBoxLayout())
		button_widget.layout().addWidget(self.submit_button)
		button_widget.layout().addWidget(self.cancel_button)
		layout.addRow('',button_widget)
		layout.addRow('Result: ', self.result)
		layout.addWidget(self.toolbar)
		layout.addWidget(self.canvas)
		layout.addWidget(self.button)
		self.setLayout(layout)
		self.cancel_button.clicked.connect(self.close)
		self.coefficient_a.textChanged.connect(self.coefinputa)
		self.coefficient_b.textChanged.connect(self.coefinputb)
		self.coefficient_c.textChanged.connect(self.coefinputc)
		self.submit_button.clicked.connect(self.authenticate)
		self.show()

	def authenticate(self):
		try: a,b,c
		except NameError: self.result.setText('Please enter values for all coefficients.')
		else: self.submit_button.clicked.connect(self.calculate)

	@qtc.pyqtSlot(str)
	def coefinputa(self, text):
		global a
		if text:
			a=[]
			try:
				number=int(text)
				a.append(text)
			except:
				self.result.setText('Invalid input')
				a.clear()
				a.append(0)
		else: 
			a.clear()
			a.append(0)

	@qtc.pyqtSlot(str)
	def coefinputb(self, text):
		global b
		if text:
			b=[]
			try:
				number=int(text)
				b.append(text)
			except:
				self.result.setText('Invalid input')
				b.clear()
				b.append(0)
		else: 
			b.clear()
			b.append(0)

	@qtc.pyqtSlot(str)
	def coefinputc(self, text):
		global c
		if text:
			c=[]
			try:
				number=int(text)
				c.append(text)
			except:
				self.result.setText('Invalid input')
				c.clear()
				c.append(0)
		else: 
			c.clear()
			c.append(0)

	def calculate(self):
		l, m, n=int(a[0]), int(b[0]), int(c[0])
		if l!=0:
			disc = (m**2) - (4*l*n)
			if disc < 0 :
				statement="The discriminant is less than zero - there are no real roots: "
				disc = math.sqrt(abs(disc)) / (2*l)
				solnthree = (-1*m) / (2*l)
				z_one, z_two = complex(solnthree,disc), complex(solnthree,-disc)
				output=str(statement)+str(z_one)+str(' & ')+str(z_two)
				self.result.setText(output)
			elif disc == 0 :
				statement="The discriminant is equal to zero - two equal real roots: "
				solnthree = (-1*m) / (2*l)
				output=str(statement)+str(solnthree)
				self.result.setText(output)
			elif disc > 0 :
				statement="The discriminant is greater than zero - two different real roots: "
				solnone = ((-1*m) / (2*l)) + ((math.sqrt(disc)) / (2*l))
				solntwo = ((-1*m) / (2*l)) - ((math.sqrt(disc)) / (2*l))
				output=str(statement)+str(solnone)+str(' & ')+str(solntwo)
				self.result.setText(output)
		else:
			if (m!=0):
				statement="The equation given is of the form:  y = mx + c. For y = 0, x = "
				output=str(statement)+str(-n/m)
				self.result.setText(output)
			else:
				if (n!=0):
					output=str("The equation given is linear. y = ")+str(n)
					self.result.setText(output)
				else:
					self.result.setText('Please enter at least one non-zero coefficient')

	def plot(self):
		x=np.linspace(-5,5,100)
		y=int(a[0])*(x**2)+(int(b[0])*x)+int(c[0])
		self.figure.clear()
		ax=self.figure.add_subplot(111)
		ax.plot(x,y,'r')
		self.canvas.draw()

if __name__=='__main__':
	app = qtw.QApplication(sys.argv) #  Always the first thing we run in any program. We're passing the cmd line arguments to this script, we need the sys library for that. 
	app.setStyle(qtw.QStyleFactory.create('Fusion'))
	w= MainWindow(windowTitle='Quadratic Solver')
	sys.exit(app.exec_())
