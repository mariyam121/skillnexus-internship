# Simple ATM Simulator

balance = 5000
correct_pin = "1234"


def check_balance():
    print("Current Balance:", balance)


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
        print("New Balance:", balance)
    else:
        print("Invalid amount.")


def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: "))

    if amount > 0 and amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining Balance:", balance)
    elif amount > balance:
        print("Insufficient balance.")
    else:
        print("Invalid amount.")


print("===== SIMPLE ATM SIMULATOR =====")

pin = input("Enter your PIN: ")

if pin == correct_pin:

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN.")