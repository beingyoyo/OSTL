class Node:
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
    def removeNode(self,key):
        curr=self.head
        prev=None
        while curr and curr.data!=key:
            prev=curr
            curr=curr.nextnode
        if prev is None:
            self.head=curr.nextnode
            self.size-=1
        elif curr:
            self.size-=1
            prev.nextnode=curr.nextnode
            curr.nextnode=None
    def printNode(self):
        curr=self.head
        while curr:
            print(curr.getData())
            curr=curr.getNextNode()

a=1
mylist=LinkedList()
while(a==1):
    c=int(input("\n1.Add\n2.Read\n3.Delete\nEnter the choice:"))
    if(c==1):
        v=int(input("Enter the value:"))
        mylist.addNode(v)
    elif(c==2):
        print("The list is:")
        mylist.printNode()
        print("The size is:",mylist.getSize())
    elif(c==3):
        d=int(input("Enter the key to be deleted:"))
        mylist.removeNode(d)
    elif(c==4):
        print("Enter the correct choice!")
        a=0

        
        
        
    
