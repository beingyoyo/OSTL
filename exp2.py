#2.1
class Vehicle:
	def __init__(self,name,kind,colour,desc):
		self.name=name
		self.kind=kind
		self.colour=colour
		self.desc=desc
	
	def display(self):
		print "Name:",self.name
		print "Kind:",self.kind
		print "Colour:",self.colour
		print "Description",self.desc

v1=Vehicle("Car1","Convertible","Red","$60,000")
v2=Vehicle("Jump","Van","Blue","$10,000")

v1.display()
print " "
v2.display()


#2.2
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def displayPerson(self):
		print "Name:",self.name
		print "Age:",self.age
class Student:
	def __init__(self,id):				
		self.id = id
	def displayStudent(self):
		print "Student id:",self.id	
class Address(Person,Student):
	def __init__(self,name,age,id):
		Person.__init__(self,name,age)
		Student.__init__(self,id)
		
	def disp(self):
		Person.displayPerson(self)
		Student.displayStudent(self)
r1 = Address("Yash",20,123)
r1.disp()
print("")
r2 = Address("Bhaven",21,456)
r2.disp()


try:
	a = int(raw_input("Enter a number: "))
	b = int(raw_input("Enter second number: "))
	
	print(a/b)
except ZeroDivisionError:
	print("Division by 0 not allowed")
except ValueError:
	print("Incorrect Datatype")
except:
	print("Enter int type of data")	
	
finally:
	print("Finally  executed.")
