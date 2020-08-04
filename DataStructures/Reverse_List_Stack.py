# Reversing lists with a stack

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

def reverse(obj):
    s=Stack()
    output=Stack()
    for i in range(0,len(obj)):
        obj_element=obj[i]
        s.push(obj_element)
    while not s.is_empty():
        output.push(s.pop())
    return output
    
my_list=[1,2,3,4,5,6,7,8]
print(reverse(my_list))
