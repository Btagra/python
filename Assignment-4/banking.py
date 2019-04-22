import collections
otp=input("Enter the four digit OTP number")
details=collections.OrderedDict()
while True:
    try:
        if otp==1234:
            print "\n","1: New Account\n", "2: Withdraw\n", "3: Deposit\n", "4: Balance inquiry\n", "5: Demand Draft\n", "6: Cancel\n"
            choice=input("Enter a number of your preference: ")
            if choice == 1:
                print "Enter the following details:"
                name, age, address, contact, gender=input("Name: "), int(input("Age: ")), input("Address: "), int(input("Contact: ")), input("Gender: ")
                print "\nAccount Holder details:\n", "Name: ", name,"\n", "Age: ", age,"\n", "Address: ", address,"\n", "Contact: ", contact,"\n", "Gender: ", gender
                details.update({"Name: ": name , "Age: ": age,"Address: ": address})
                details.update({"Contact: ": contact, "Gender: ": gender})
            elif choice == 2:
                x=input("Enter the amount to withdraw: ")
                if x>100 and x<10000:
                    print "HERE IS YOUR MONEY"
                    details.update({"Withdraw: ": x})
                else:
                    print "LIMIT EXCEEDED"
            elif choice == 3:
                x=input("Enter the amount of deposit: ")
                if x%5==0:
                    print "AMOUNT DEPOSITED" 
                    details.update({"Deposit: ": x})  
                else:
                    print "ENTER THE VALID AMOUNT"
            elif choice == 4:
                print "1: Deposit Amount\n", "2: Outstanding balance\n", "3: Minimum Due Amount"
                choice1=input("Enter the choice: ")
                x=("Deposit Amount" if choice1==1 else "Outstanding balance" if choice1==2 else "Minimum Due Amount" if choice1==3 else "Wrong selection")
                details.update({"Balance Inquiry: ": x})
            elif choice == 5:
                print "Enter the details of Demand Draft:"
                bankname, accountholder, branch, totalamount=input("Name of Bank: "), input("Name of Account Holder: "), input("Name of Branch: "), int(input("Total Amount: "))
                details.update({"Name of Bank: ": bankname , "Name of Account Holder: ": accountholder, "Name of Branch: ": branch, "Total Amount: ": totalamount})
            elif choice == 6:
                for k,v in details.items():
                    print k,v
                break
        else:
            print "Sorry try again"
            break
    except:
        print "Enter valid input"