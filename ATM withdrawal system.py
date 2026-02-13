# ATM Withdrawal Simulation

balance = 10000

print("Welcome to ATM")
print("Initial Balance: ₹", balance)

while True:
    try:
        amount = float(input("\nEnter withdrawal amount (or 0 to exit): "))

        if amount == 0:
            print("Thank you for using ATM.")
            break

        if amount <= 0:
            raise Exception("Amount must be greater than zero.")

        if amount > balance:
            raise Exception("Insufficient balance.")

        balance -= amount
        print(f"Withdrawal successful! Remaining Balance: ₹{balance}")

    except ValueError:
        print("Invalid input! Please enter a number.")
    except Exception as e:
        print("Error:", e)
