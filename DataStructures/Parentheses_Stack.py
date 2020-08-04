class Stack():
	def __init__(self):
		self.stack = list() 
	def push(self, item):
		self.stack.append(item) 
	def pop(self):
		if len(self.stack)>0: 
			return self.stack.pop()
		else:
			return None
	def is_empty(self):
		if self.stack==[]:
			return True
		else:
			return False
	def __str__(self): 
		return str(self.stack)

# use a stack to deterine whether or not a string has balanced use of parenthesis

def match_check(p1,p2):
	if (p1 == "(" and p2==")") or (p1 == "{" and p2=="}") or (p1 == "[" and p2=="]"):
		return True
	else:
		return False

def balance_check(string):
	mystack=Stack()
	balanced=True
	i=0
	while (i < len(string)) and (balanced == True):
		string_element=string[i]
		if string_element in "{[(":
			mystack.push(string_element)
		if string_element in "}])":
			if mystack.is_empty():
				balanced=False
			else:
				top=mystack.pop()
				if not match_check(top,string_element):
					balanced=False
		else:
			i+=1
			continue
		i+=1
	if mystack.is_empty() and balanced ==  True:
		return True
	else: 
		return False

def main():
	string1=("[a[aa[a]a{a}98-&a(a)(a(a)a)a]a]")
	string2=("[a[aa[a]a{a}98,())-&a(a)(a(a)a)a]a]")
	print(balance_check(string1),balance_check(string2))

if __name__ == '__main__':
	main()
