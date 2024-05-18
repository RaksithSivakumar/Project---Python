import time

print("Please insert Your CARD")

time.sleep(5)  

password = 1234

pin = int(input("Enter your ATM pin: "))

balance = 5000

if pin == password:
    while True:
        print("""
        1 == Balance
        2 == Withdraw Balance
        3 == Deposit Balance
        4 == Exit
        """)

        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")

        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            if withdraw_amount > balance:
                print("Insufficient balance")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your current balance is {balance}")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")

        elif option == 4:
            print("Thank you for using our ATM!")
            break

        else:
            print("Please enter a valid option")

else:
    print("Incorrect pin")
