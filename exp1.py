#Swap 2 nos.
x=int(input("Enter a no:"))
y=int(input("Enter a no:"))
x,y=y,x
if(x>0):
 print("Number is positive")
elif(x<0):
 print("Number is negative")
else:
 print("Number is 0")

#Menu driven to check if the number and string are palindrome

print("Menu\n1.number\n2.string")
c=input()
if c==1:
    a=int(input('enter a number: '))
    temp=a
    rev=0
    while(a>0):
        no=a%10
        rev=rev*10+no
        a=a/10
    if(temp==rev):
        print('the number is palindrome')
    else:
        print('the number is not palindrome')
if c==2:
    b=raw_input('Enter the string: ')
    d= b[::-1]
    if b==d:
        print('the string is palindrome')
    else:
	print('the number is not palindrome')

#Program to demonstrate use of list 

even=range(0,10,2)
odd=range(1,10,2)
print even
print odd
c=int(input("Menu\n1.Merge and Sort\n2.Updation and Deletion\n3.Minimum and Maximum\n4.Name Check\n"))
if(c==1):
 merge=even+odd
 print merge
 merge.sort()
 print merge
elif(c==2):
 del even[len(even)/2]
 print even
 del odd[len(odd)/2]
 print odd
 even[0] = 12
 print even
 odd[0] = 11
 print odd
elif(c==3):
 max1=max(even)
 print max1
 max2=max(odd)
 print max2
 min1=min(even)
 print min1
 min2=min(odd)
 print min2
else:
 n=input("Enter the number of name:")
 for i in range(0,n):
  s= raw_input("Enter a name: ")
  if s in even:
   print "Already there"
  else:
   even.append(s)
 print even 



#Demonstrate tuples in python
print "1.Add element\n2.Display\n3.Nested Tuple\n"
c = input("Enter choice: ")
l=[("Python",31,65,85,67)]

if c==1:
    n = input("Enter number of entries: ")
    
    for i in range(0,n):
        l1 = []
        a = raw_input("Enter name: ")
        l1.append(a)
        b = int(input("Enter roll number: "))
        l1.append(b)
        c = input("Enter marks of 3 subjects: ")
        d = input()
        e = input()
        l1.append(c)
        l1.append(d)
        l1.append(e)
        x = tuple(l1)
        l.append(x)
    print l

elif c==2:
    for i in l:
        if "Python" in i:
            print i     

elif c==3:
    t = (("Python",1),("Perl",2),("Pascal",3))
    sorted(t)       
    t1 = tuple(t)
    print t1
#SETS

a = raw_input("enter 1st string: ")
b = raw_input("enter 2nd string: ")
s1 = set(a)
s2 = set(b)

print "1.intersection\n2.union\n3.characters in s1 but not in s2\n4.symmetric difference\n"

c = input("Enter choice: ")

if c==1:
    print s1&s2

elif c==2:
    print s1|s2
    
elif c==3:
    print s1-s2
    
elif c==4:
    print s1.symmetric_difference(s2)

#Dictionary

d = {1:'A',2:'B',3:'C'}
l = []
print ("1.Update\n2.Delete\n3.Search\n4.Map\n")

c = input("Enter choice: ")

if c==1:
    n = input("Enter number of entries: ")
    for i in range(0,n):
        x = input("Enter key: ")
        y = raw_input("Enter value: ")
        l1 = []
        l1.append(x)
        l1.append(y)
        l.append(l1)
    
    for j in l:
        d[j[0]] = j[1]
    print d
    
elif c==2:
    s = input("Enter key to be deleted: ")
    del d[s]
    print d

elif c==3: 
    s = input("Enter key to be searched: ")
    
    if s in d:
        print "Value of key is:",d[s]
    else:
        print "Key not found"
else:
    key=[1,2,3,4]
    value=['a','b','c','d']
    print "\nMap list is: "
    d1= dict(zip(key,value))
    print d1
  
