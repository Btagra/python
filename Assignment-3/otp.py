import random
randNum=random.randrange(1,20)
fname, lname = input("Enter your First Name : "), input("Enter your Last Name : ")
print ("Hello " + fname + " " + lname)
for i in range(0,4):
    otp=input("Enter the OTP from 1 to 20: ")
    if otp<=20:
        if otp==randNum:
            print "OTP SUCCESSFULLY MATCHED"
            break
        elif i==3:
            print "SORRY PROGRAM CRASHED" 
        else:
            print "ERROR!!!ENTER THE OTP AGAIN"
            x=input("Want to continue yes or no: ")              
            if x=="no":
                print "Thanks for attempt"
                break
    else:
        print "Try Again! Wrong Input"
        break