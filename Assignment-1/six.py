#Write a program to implement the nested and ladder if else condition.

#Nested if-else condition:
age = 38
if (age<11):
    print "You're not eligible to buy ticket"
elif (age>=11):
    print "You are eligible to buy ticket"
    if (age <=20 or age >=60):
        print "Ticket price: $12"
    else:
        print "Ticket price: $20"


#Ladder if-else condition:
x = int(raw_input("Enter the value"))
if (x<10):
    print "x is less than 10"
if (x>=10 and x<=20):
    print "x is between 10 to 20"
if (x>20 and x<50):
    print "x is between 20 to 50"
else:
    print "x ix greater than 50"
