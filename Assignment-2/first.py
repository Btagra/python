# Write a program to take out the element from their index values:
x=[1,2,3,4,[10,20,30,40,[100,200,300,400],"riyazulhaque",5+5j],4000]
print x

#[10,20]
print x[4][0:2]

#(5+5j)
print x[4][6]

#[300,400]
print x[4][4][2:5]

#[40,[100,200,300,400],"riyazulhaque"]
print x[4][3:6]