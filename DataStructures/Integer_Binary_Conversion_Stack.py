# converting integers to binary using a stack

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

def div_by_2(int_num):
    s=Stack()
    while int_num > 0:
        remainder = int_num % 2
        s.push(remainder)
        int_num=int_num//2
    binary_number =""
    while not s.is_empty():
        binary_number+=str(s.pop())
    return binary_number

def main():
	print(div_by_2(2))
	print(div_by_2(3))
	print(div_by_2(4))
	print(div_by_2(7))
	print(div_by_2(8))
	print(div_by_2(16))

if __name__ == "__main__":
	main()
