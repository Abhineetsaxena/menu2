#!/usr/bin/python36

print("content-type: text/html")
print()

import cgi


print("This is master slave hadoop structure")
slave_nums=cgi.FieldStorage().getvalue('slave_num')
sn=int(slave_nums)

i=1
print("Enter IPs of slaves <br>")
while sn !=0:
	print("<input name={}>".format(i))
	#print(sn)	
	sn=sn-1
	print("<br>")
	#print(i)
	i=i+1
	
print("<br>Enter ip of Master : <input name='mip'>")
print("<br>Enter ip of Clinet : <input name='cip'>")
print("<input type='submit' value='submit'>")


#Menu2

