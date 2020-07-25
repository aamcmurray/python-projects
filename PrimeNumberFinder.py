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

def main():
	ceiling = 10000000
	M=list(bool_flipper(ceiling))
	print("primes found: ", len(M))

if __name__ == "__main__":
	main()
