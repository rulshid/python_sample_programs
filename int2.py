#Given a String of length N reverse the words in it. Words are separated by space without using any library method
#python2.7
a=raw_input("string")
a=a[::-1]
#print a
a=a.split()
#print a
b=a[0]
for i in range(1,len(a)):
     b=b+" "+a[i]
print b
