import pymysql
a=0
db=pymysql.connect(host="localhost",user="root",password="yash",db="yash")

try:
	c=db.cursor()
	
	def insert(db):
		with db.cursor() as c:
			name=input("Enter a name:")
			id=int(input("Enter the ID:"))
			t=("INSERT INTO emp VALUES(%s,%s)")
			c.execute(t,(id,name))
			print("Successfully Added!")
			db.commit()
	
	def read(db):
		with db.cursor() as c:
			c.execute("SELECT * FROM emp")
			r=c.fetchall()
			for i in r:
				print (i)
		n=r
		print(n)
	def update(db):
		with db.cursor() as c:
			name=raw_input("Enter a name:")
			id=int(input("Enter the ID whose name you wish to update:"))
			t1=("UPDATE emp SET name=%s WHERE id=%s")
			c.execute(t1,(name,id))
			print("Successfully Updated!")
			db.commit()
	def delete(db):
		with db.cursor() as c:
			id=int(input("Enter the ID to be deleted:"))
			t2=("DELETE FROM emp WHERE id=%s")
			c.execute(t2,(id))
			print("Successfully Deleted!")
			db.commit()
	while(a==0):
		opt=int(input("1.Insert\n2.Update\n3.Delete\n4.Read\nEnter your choice:"))
		if(opt==1):
			insert(db)
		elif(opt==2):
			update(db)
		elif(opt==3):
			delete(db)
		elif(opt==4):
			read(db)
		else:
			print("Enter correct choice!")
			a=1

finally:
	db.close()
'''	

--------------OUTPUT---------------
c065@comp:~$ python database.py
1.Insert
2.Update
3.Delete
4.Read
Enter your choice:1
Enter a name:Bhaven
Enter the ID:1
Successfully Added!
1.Insert
2.Update
3.Delete
4.Read
Enter your choice:4
(2, 'Yash')
(3, 'Dhairya')
(1, 'Bhaven')
1.Insert
2.Update
3.Delete
4.Read
Enter your choice:2
Enter a name:Advait
Enter the ID whose name you wish to update:3
Successfully Updated!
1.Insert
2.Update
3.Delete
4.Read
Enter your choice:4
(2, 'Yash')
(3, 'Advait')
(1, 'Bhaven')
1.Insert
2.Update
3.Delete
4.Read
Enter your choice:3
Enter the ID to be deleted:3
Successfully Deleted!
1.Insert
2.Update
3.Delete
4.Read
Enter your choice:4
(2, 'Yash')
(1, 'Bhaven')
1.Insert
2.Update
3.Delete
4.Read
Enter your choice:5
Enter correct choice!
c065@comp:~$ 
'''
