# Using an altered stack type to find the sum of numbers divisible by 3 or 5. 

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
    def smelt(self):
        B=set()
        for i in range(len(self.stack)):
            B.add(self.stack.pop())
        return B
    def __str__(self): 
        return str(self.stack)

def stack_filler(n,c,stackobj):
    for i in range(0, c):
        if i%n==0:
            stackobj.push(i)
    return stackobj

def main():
    ceiling=1000
    a=3
    b=5
    my_stack=Stack()
    my_second_stack=Stack()
    print(sum(stack_filler(a,ceiling,my_stack).smelt()|stack_filler(b,ceiling,my_stack).smelt()))
    
if __name__ == "__main__":
    main()
