import urllib.request
import urllib.parse
response=urllib.request.urlopen('http://nebulus.aitm.edu.in/')
bytecode=response.read()
htmlstr=bytecode.decode()
print(htmlstr)
