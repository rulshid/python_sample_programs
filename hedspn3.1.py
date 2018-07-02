#python2.7
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
n=100
summ=0
sum_of_sqr=0
#n=input("enter number")
for i in range(1,n+1):
    summ=summ+i
    sum_of_sqr=sum_of_sqr+i*i
print (summ)*summ-sum_of_sqr

