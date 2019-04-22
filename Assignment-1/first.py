#Write a program to take input from user using following approach and return the datatype of all variable:

#raw_input()
x = raw_input("What is you name?")
print x
print type(x)

x = raw_input("Enter the age")
print x
print type(x)

#raw_input with type conversion
x = int(raw_input("Enter the age"))
print x
print type(x)

#raw_input with eval
x = eval(raw_input("Enter the value"))
print x
print type(x)

#input in version 2
x = input("Enter the value")
print x
print type(x)

#input in version 3
x = input("Enter the age")
print(x)
print (type(x))

x = int(input("Enter the value"))
print(x)
print (type(x))

