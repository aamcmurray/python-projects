# AppliedMaths 
A folder containing some methods for dealing with various maths problems. 
  - Derivatives: Using finite differences methods with numpy and matplot lib to find approximate solutions to differentiation problems.
  - ODESolve: A solver for ordinary differential equations using sklearn and scipy.
  - QuadraticSolver: A solver for quadratic equations including matplotlib visualisation.
  
# Bayesian Analysis
A folder containing methods for Bayesian analysis, mostly fitting.
  - Bayesian Introduction: Reproduced following a tutorial by Simon Ouellette. Useful reference.
  - An attempt at a non linear regression using some fake data generated using the damped harmonic motion equation and solving for the coefficients. 
  - Fitting comparison: Attempt at comparing non linear regression via scipy to bayesian fit. 
  - LeastSquaresComparison: Attempt at comparing linear least squares method to bayesian fit.

# Data Structures
A folder containing practice using different data structures.
  - IntToBinaryStack: Converts integers to binary using a stack. 
  - NumberTheory Stack: Using an altered stack with a method for decomposing its contents to a set to find the sum of numbers divisible by 3 and 5. 
  - Parentheses Stack: Using a stack to determine if parentheses are balanced or not. 
  - Reverse Stack: Using a stack to reverse list.
  
# NumberTheory 
A folder containing code relating to number theory. 
  - JuliaSetGifMaker: Uses a recursive procedure to draw a Julia set, given a range, for instance x+iy with y from -2 to 2, it will generate multiple images and collect them in a .gif format. Uses PIL.
  - MandelbrotSetImager: Uses a recursive procedure to generate images of the mandelbrot set. Uses PIL.
  - PrimeNumberFinder: A relatively efficient prime number finder, uses an erastasthones sieve, skips the even numbers and only calculates to sqrt(N). 

# Project Euler Folder.
A folder with solutions to various project euler (https://projecteuler.net/archives) problems. 

# Regression
A folder containing various tools, methods, approaches to regression and analysis. 
  - Fitting tools: Includes integration, interpolation, linear regression, analysis tools multivariate regression via sklearn... etc.
  
# SimpleMonteCarlo.
A folder containing simple monte carlo solutions. 
  - ApproximatePi: Approximates pi.
  - Integration: Finds area under a curve via SMC.

# ClonogenicsSurvivalCurveFitting.py

Reads in clonogenic assay data from a .csv file using pandas library. Uses numpy to replace blank entries with NaN values. Takes average count of a 6 well plate, standard deviation and SEM accounting for missing or NaN entries. Averages over any replicates by finding entries with the same dose using fancy indexing. Calculates the plating efficiency of the control and the survival fractions and normalised survival fractions. Plots the normalised survival fractions against dose /Gy in a scatter plot. Fits the data using a non-linear regression using the SciPy library. Returns alpha and beta values with standard deviation calculated by the covariance diagonal. 

# MockClonogenicData.csv

Contains some mock data for ClonogenicsSurvivalCurveFitting.py 

# README.md

# SafeDiveTest.py

Determines if a planned dive exceeds the British Sub Aqua Club guidelines on Oxygen partial pressure levels. Complete with some validation layers. This is not endorsed by or affiliated with BSAC. It's a code written for personal use based on their safety guidelines.
