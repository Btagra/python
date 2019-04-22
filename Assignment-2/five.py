# Write a program to print the copy of list which has all the element multiplied
# by 3 but it should not reflect the result to the original list.
import copy
x=[1,2,3,4,5,5,7]
y=copy.copy(x)
y=[i*3 for i in y]
print "Original list:",x
print "Copy of list with multiplication 3:", y