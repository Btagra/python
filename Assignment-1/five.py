#Write a program to enter the number and print "Yes I am in the range" 
#if it is in range of 10-50 if not and then print "Oops".

x = int(raw_input("Enter the number"))
if(x>10 and x<50):
    print "Yes I am in the range"
else:
    print "Oops"
