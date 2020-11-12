a=[1,2,3,4,5]
b=[1,2,3,4,5]

def LeftRotator(inputlist):
	first=inputlist[0]
	for i in range(0,len(inputlist)):
		if i<len(inputlist)-1:
			inputlist[i]=inputlist[i+1]
		else:
			inputlist[i]=first
	return inputlist

def RightRotator(inputlist):
	first=inputlist[len(inputlist)-1]
	for i in reversed(range(len(inputlist))):
		if i!=0:
			inputlist[i]=inputlist[i-1]
		else:
			inputlist[i]=first
	return inputlist

print(a, LeftRotator(LeftRotator(b)), RightRotator(RightRotator(a)))
