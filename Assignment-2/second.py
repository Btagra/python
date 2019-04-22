# Write a program to take out the pair of numbers whose sum is equal to an even number.
# You should return the list from the range of 1 to 21.
x=range(1,22)
print x
y=[]
for i in range(len(x)):
    for j in range((i+1),len(x)):
        sum=x[i]+x[j]
        if sum%2==0:
            y.append ((x[i],x[j]))
print y  