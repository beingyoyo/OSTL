'''class Node:
	def __init__(self,data,nextnode=None):
		self.data=data
		self.nextnode=nextnode
	def getData(self):
		return self.data
	def setData(self,val):
		self.data=val
	def getNextNode(self):
		return self.nextnode
	def setNextNode(self,val):
		self.nextnode=val

class LinkedList:
	def __init__(self,head=None):
		self.head=head
		self.size=0
	def getSize(self):
		return self.size
	def addNode(self,data):
		newNode=Node(data,self.head)
		self.head=newNode
		self.size+=1
		return True
	def printNode(self):
		curr=self.head
		while curr:
			print (curr.getData())
			curr=curr.getNextNode()
mylist=LinkedList()
print("Inserting")
print(mylist.addNode(15))
print(mylist.addNode(10))
print("Printing the node")
mylist.printNode()
print(mylist.getSize())           	
---------OUTPUT--------------
c502@comp:~$ python ds.py
Inserting
True
True
Printing the node
10
15
2
'''

'''class Stack:
	def __init__(self):
		self.items=[]
	def isEmpty(self):
		return self.items==[]
	def push(self,items):
		self.items.append(items)
		return items
	def pop(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[len(self.items)-1]
k=Stack()
print(k.isEmpty())
print ("value:",k.push(20))
print ("value:",k.push(12))
print ("size of stack:",k.size())
print("Element pop is",k.pop())
print ("size of stack:",k.size())
print ("Peek:",k.peek())
========OUTPUT===============
True
value: 20
value: 12
size of stack: 2
Element pop is 12
size of stack: 1
Peek: 20
'''


#3.3
class Queue:
	def __init__(self):
		self.items=[]
	def isEmpty(self):
		return self.items==[]
	def insert(self,item):
		self.items.insert(0,item)
		return item
	def delete(self):
		return self.items.pop()
	def size(self):
		return len(self.items)

q=Queue()
print(q.isEmpty())
print ("Value",q.insert(50))
print ("Value",q.insert(40))
print ("Value",q.insert(10))
print("element at front",q.delete())
print("size of queue",q.size())

--------OUTPUT----------
c502@comp:~$ python ds.py
True
Value 50
Value 40
Value 10
element at front 50
size of queue 2


