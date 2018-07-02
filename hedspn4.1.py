n=1000
summ=0
#n=input("enter number")
for i in range(1,n):
    
    if (i%4)==0 or (i%5)==0:
         summ=summ+i
print summ
