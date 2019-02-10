import re as r

#Simple matching String

#r stands for raw string
pattern = r"eggs"

if r.match(pattern,"eggseggseggs09"):
#Match function for Extact Match of string
    print("match found")
else:
    print("No Match Found")



#pattern is present any where in the string
if r.search(pattern,"baconeggseggseggsbacon"):
#if re.match(pattern,"bacconeggseggs"):
    print("match found")
else:
    print("No Match Found")



if r.findall(pattern,"baconeggseggseggsbacon"):
#if re.match(pattern,"bacconeggseggs"):
    print("match found")
else:
    print("No Match Found")


print(r.findall(pattern,"baconeggseggseggsbacon"))


#FIND AND REPLACE
string ="My name is John, I'm John"
pattern =r"John"
newstring = r.sub(pattern,"Rob",string)
print(newstring)
#meta chracters  to make RE more strong
#very first metacharacters is dot
#instead of dot accept any char
pattern = r"gr.y"
if r.match(pattern,"grey"):
#if r.match(pattern, "eggsgrey"): false
    print("match fouund")
#CARET [^] AND DOLLER[$] META CHARACTER
#used in django for url pattern
pattern =r"^gr.y$"
if r.match(pattern,"grey"):
#if r.match(pattern, "grbs"): false  if grey or gray wud b true
    print("match fouund")
#CHARACTER CLASSES
#address street like AA1
#AA1
pattern = r"[A-Z][A-Z][0-9]"

if r.search(pattern,"AH6"):
    print("Match Found")
#STAR METACHARACTER
pattern =r"eggs(bacon)*"

if r.match(pattern,"eggsbacconbacon"):
#eggs should be first any how
#bacon we can right 0times 1 times or multiple
# times if bacon ..false if eggsbacon ..true if eggsbaacon
  print("Match Found")











#Group Match

pattern =r"bread(eggs)*bread"
#if we have breadbread ...true  if breadeggseggsbread true
if r.match(pattern,"breadeggseggsbread"):
    print("match Found")










