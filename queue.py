class Queue:
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def insert(self,val):
        self.item.insert(0,val)
        return self.item
    def pop(self):
        return self.item.pop()
    def size(self):
        if(len(self.item)==0):
            print("Queue Empty")
        else:
            return len(self.item)
    def peek(self):
        return self.item[len(self.item)-1]

q=Queue()
a=1
while(a==1):
    c=int(input("\n1.Insert\n2.Delete\n3.Peek\n4.Size\nEnter the choice:"))
    if(c==1):
        v=int(input("Enter the value:"))
        q.insert(v)
    elif(c==3):
        print("The front is at:",q.peek())
    elif(c==2):
        q.pop()
    elif(c==4):
    	print("Queue size is:",q.size())
    elif(c==5):
        print("Enter the correct choice!")
        a=0
