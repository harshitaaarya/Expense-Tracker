print("Welcome to Expense Tracker <3")

expenses = []   # List to store expenses

while True:
    print("\n|||||| MENU ||||||")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Please enter 1/2/3/4: ")

    # Add Expense
    if choice == "1":
        date = input("Date of expense: ")
        category = input("Category: ")
        description = input("Description: ")
        amount = float(input("Amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    # View All Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\n----- Your Expenses -----")
            count = 1
            for eachexpense in expenses:
                print(
                    f"Expense {count} -> "
                    f"{eachexpense['date']}, "
                    f"{eachexpense['category']}, "
                    f"{eachexpense['description']}, "
                    f"{eachexpense['amount']}"
                )
                count += 1

    # View Total Expense
    elif choice == "3":
        total = 0
        for eachexpense in expenses:
            total += eachexpense["amount"]

        print(f"\nTotal Expense = {total}")

    # Exit
    elif choice == "4":
        print("Thanks for using this system!")
        break

    else:
        print("Choose between 1, 2, 3, and 4.")
