print("Welcome to Pentagon ATM")
card = input("Insert your card (yes/no): ")
if card == "yes":
    print("Card accepted.")
    pin = input("Enter your 4-digit PIN: ")
    if pin == "1234":
        print("PIN correct.")
        print("Press 1 for English")
        print("Press 2 for Hindi")
        print("Press 3 for Maithili")
        print("Press 4 for Kannada")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You selected English")
        elif choice == "2":
            print("You selected Hindi")
        elif choice == "3":
            print("You selected Maithili")
        elif choice == "4":
            print("You selected Kannada")
        else:
            print("Invalid choice")
        balance = float(input("Enter your current balance: "))
        amount = float(input("Enter your withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            new_balance = balance - amount
            print("Transaction successful.")
            check = input("Do you want to check your balance? (yes/no): ").strip().lower()
            if check == "yes":
                print("Your current balance is ",new_balance)
                print("Thank you, visit again.")
            else:
                print("Thank you, visit again.")
    else:
        print("Incorrect PIN. Try again with the correct PIN.")
else:
    print("Card not inserted properly. Transaction cancelled.")
