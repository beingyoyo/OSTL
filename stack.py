class Stack:
	def __init__(self):
		self.item=[]
	def isEmpty(self):
		return self.item==[]
	def push(self,val):
		self.item.append(val)
		return self.item
	def pop(self):
		return self.item.pop()
	def size(self):
		if(len(self.item)==0):
			print("Stack Empty")
		else:
			return len(self.item)
	def peek(self):
		return self.item[len(self.item)-1]

s=Stack()
a=1
while(a==1):
    c=int(input("\n1.Push\n2.Pop\n3.Peek\n4.Size\nEnter the choice:"))
    if(c==1):
        v=int(input("Enter the value:"))
        s.push(v)
    elif(c==3):
        print("The top is at:",s.peek())
    elif(c==2):
        s.pop()
    elif(c==4):
    	print("Stack size is:",s.size())
    elif(c==5):
        print("Enter the correct choice!")
        a=0

