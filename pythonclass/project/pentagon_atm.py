import time
password=1234
Balance=10000
print("Welcome to Pentagon ATM")
print("Insert your card")
print("press 1.yes 2.no")
card=int(input())
if card==1:
    print("enter your pin")
    pin=int(input())
    if pin==password:
        print("select your language")
        print("Press 1.english 2.kannada 3.hindi")
        lang=int(input())
        if lang==1:
            print("select the option")
            print("press 1.Bal enq  2.withdrawl")
            choice=int(input())
            if choice==1:
                print("your available balance is",Balance)
            elif choice==2:
                print("enter the amount")
                amt=int(input())
                if amt<=Balance and amt>0 and amt%100==0:
                    print("your transaction is proccessing")
                    time.sleep(5)
                    print("collect your cash")
                    time.sleep(4)
                    print("do you want to check your balance")
                    print("press 1.yes 2.no")
                    choice1=int(input())
                    if choice1==1:
                        print("your available balance is",Balance-amt)
                        print("Thank you visist again")
                    else:
                        print("Thank you visist again")
                else:
                    print("invalid amount")
            else:
                print("invalid option")
        else:
            print("Please select only english")
    else:
        print("wrong pin")
else:
    print("Insert your card properly")