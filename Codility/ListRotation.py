an=[1,2,3,4,5]
bn=[1,2,3,4,5]
cn=[]

def LeftRotator(inputlist, times):
	if len(inputlist)>0:
		count=0
		while count<times:
			first=inputlist[0]
			for i in range(0,len(inputlist)):
				if i<len(inputlist)-1:
					inputlist[i]=inputlist[i+1]
				else:
					inputlist[i]=first
			count+=1
		return inputlist
	else:
		return inputlist


def RightRotator(inputlist,times):
	if len(inputlist)>0:
		count=0
		while count<times:
			first=inputlist[len(inputlist)-1]
			for i in reversed(range(len(inputlist))):
				if i!=0:
					inputlist[i]=inputlist[i-1]
				else:
					inputlist[i]=first
			count+=1
		return inputlist
	else:
		return inputlist
