#  =================================================================================
#  ___________________________________________________________A Prime Number finder_
#  ___________________________________________________________ver. 6________________
#  ___________________________________________________________24/07/2020____________
#  =================================================================================
#  Description
#  =================================================================================
#  A function which, for some given ceiling input, will find the primes up to that number. It does so by creating a list of True/False values. False values are attributed to even numbers. True values are attributes to odd numbers. As it goes through the list it: (i) ignores false values and continues (ii) yields the index of true values and proceeds to eliminate its multiples.
#
#  =================================================================================
#  Version History
#  =================================================================================
#
#  v.1. (220720) - Was initially a simple factor finder which returned a number as prime if it failed to find more factors than 1 and the number itself. 
#  v.2. (220720) - Skipped checking if even numbers were prime.
#  v.3. (220720) - Cut the checking by half. If the prime, N, was being checked for factors, the function would stop at N/2
#  v.4. (230720) - After building a factor finder, realised it was sufficient to stop checking at sqrt(N). Implimented this.
#  v.5. (240720) - Rather than checking every number for factors, it is possible to go through a list of numbers and eliminate their multiples (eliminating non primes) and producing a list of what is left. Implimented this using a numpy array of size N filled with 1s. 
# v.6 Current (240720) - (i) Got rid of imports and changed to a list of bool values since a numpy array [1,0,1] is 216 bytes size while a list [True, False, True] is only 132. (ii) Made it a function.
#
#  =================================================================================
#  The Code
#  =================================================================================
#

def bool_flipper(C):
	prime=2*[False]+2*[True]+int(((C-2)/2))*[False, True]
	yield 2
	i = 3
	while (i^2) <= C:
		if prime[i] == False:
			i += 1
			continue
		elif prime[i] == True:
			yield i
			j = 2*i
			while j < C:
				prime[j] = False
				j += i
			i += 2
	return

ceiling = 10000000
M=list(bool_flipper(ceiling))
print("primes found: ", len(M))

