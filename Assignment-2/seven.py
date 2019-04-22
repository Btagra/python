# Write a program to return True if the list consist only integer values only and if not return false.

#The isinstance() function returns True if the specified object is of the specified type, otherwise False.
res=all(isinstance(x, int) for x in [1,2,3,4])
print res
res=all(isinstance(x, int) for x in [1,"hello",3,4,5,8,10])
print res

#The any() function returns True if any item in an iterable are true, otherwise it returns False.
res=not any(not isinstance(y,(int)) for y in [1,2,3])
print res
res=not any(not isinstance(y,(int)) for y in [1,"2",3])
print res
