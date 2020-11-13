# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing. Goal is to find that missing element. Given: N is an integer within the range [0..100,000]; the elements of A are all distinct; each element of array A is an integer within the range [1..(N + 1)].

def solution(A):
	B=[i+1 for i in range(len(A)+1)]
	unique=set(B).difference(A)
	return unique.pop()
