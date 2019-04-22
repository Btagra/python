#Write a program to print "Hurray it is what I am looking for" if the number is divisible 
#by both 2 and 5 and if it is not and print "wrong input". Make sure that you allow user to 
#input the value from keyboard.

x = int(raw_input("Enter the number"))
if(x%2==0 and x%5==0):
    print "Hurray it is What I am looking for"
else:
    print "Wrong input"
