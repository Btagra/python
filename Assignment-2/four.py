# Write a program to print the list of numbers which has a cube
# of odd numbers in the range of 1,50.
x=range(1,51)
print x

for i in range(len(x)):
    x[i]=x[i]**3

res= filter(lambda x:x%2 > 0, x)
print res