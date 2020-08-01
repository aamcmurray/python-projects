# AppliedMaths 
A folder containing some methods for dealing with various maths problems. 
  - ODESolve: A solver for ordinary differential equations using sklearn and scipy.
  - QuadraticSolver: A solver for quadratic equations including matplotlib visualisation.
  
# NumberTheory 
A folder containing code relating to number theory. 
  - JuliaSetGifMaker: Uses a recursive procedure to draw a Julia set, given a range, for instance x+iy with y from -2 to 2, it will generate multiple images and collect them in a .gif format. Uses PIL.
  - MandelbrotSetImager: Uses a recursive procedure to generate images of the mandelbrot set. Uses PIL.
  - PrimeNumberFinder: A relatively efficient prime number finder, uses an erastasthones sieve, skips the even numbers and only calculates to sqrt(N). 

# Project Euler Folder.
A folder with solutions to various project euler (https://projecteuler.net/archives) problems. 
  
# SimpleMonteCarlo.
A folder containing simple monte carlo solutions. 
  - ApproximatePi: Approximates pi.
  - Integration: Finds area under a curve via SMC.

# BayesianInference_Beta_Binomial

Attempt at simple bayesian model using a uniform distribution prior and a binomial likelihood distribution to evaluate a posterior. Estimates proportion of google earth entries which feature the united kingdom and ireland given some initial observations. uniform selected to assume zero prior knoweldge of what proportion might be. binomial selected as it's a discrete probability distribution for number of successes given N binary success/failure trails. Used jupyter notebook. 

# ClonogenicsSurvivalCurveFitting.py

Reads in clonogenic assay data from a .csv file using pandas library. Uses numpy to replace blank entries with NaN values. Takes average count of a 6 well plate, standard deviation and SEM accounting for missing or NaN entries. Averages over any replicates by finding entries with the same dose using fancy indexing. Calculates the plating efficiency of the control and the survival fractions and normalised survival fractions. Plots the normalised survival fractions against dose /Gy in a scatter plot. Fits the data using a non-linear regression using the SciPy library. Returns alpha and beta values with standard deviation calculated by the covariance diagonal. 

# Fittingv2

Fitting some fake data using standard SciPy nonlinear regression and an attempt at a bayesian approach. 

# LeastSqaures

Comparing least squares to a Bayesian linear regression. Bayesian inference gives a best bit but also a whole posterior distribution of likely parameters. 

# MockClonogenicData.csv

Contains some mock data for ClonogenicsSurvivalCurveFitting.py 

# README.md

# SafeDiveTest.py

Determines if a planned dive exceeds the British Sub Aqua Club guidelines on Oxygen partial pressure levels. Complete with some validation layers. This is not endorsed by or affiliated with BSAC. It's a code written for personal use based on their safety guidelines.
