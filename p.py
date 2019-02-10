'''#3.1
fo=open("Yash.txt",'a+')
fo.write("Hello\n")
fo.close()
fo=open("Yash.txt",'r')
str=fo.read()
print ("File contents:",str)
fo.close()
'''
#3.2
num_w=0
num_c=0
num_line=0
fh=open("Yash.txt",'r')
#fh.read()
str=fh.read()
print ("File contents:",str)
for line in fh:
	num_line+=1
	num_c+=len(line)
	words=line.split()
	num_w+=len(words)
print("No.of words",num_w)
print("No.of lines",num_line)
print("No.of characters",num_c)
fh.close()
