numbers=[1,1,1,1,0,0,1,1,0,3,1,7]

def solution(A):
	seen=set()
	dupes=set()
	if len(A)>0:
		for i in range(0, len(A)):
			if A[i] not in seen:
				seen.add(A[i])
			else:
				if A[i] not in dupes:
					dupes.add(A[i])
				continue
		uniques=set(seen).difference(dupes)
		for i in range(0,len(uniques)):
			yield uniques.pop()
	else:
		return None

print(list(solution(numbers)))
