# Expense Tracker
expenseslist = []

print("Welcome to Expense Tracker")

while True:
    print("==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        date = input("Date of expense: ")
        category = input("Category (FOOD, CLOTHES, TRAVEL): ")
        description = input("Extra details: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenseslist.append(expense)
        print("\nExpense added successfully.")

    elif choice == "2":
        if len(expenseslist) == 0:
            print("No expenses added.")
        else:
            print("==== YOUR EXPENSES ====")
            count = 1

            for each_expense in expenseslist:
                print(
                    f"Expense {count} -> "
                    f"{each_expense['date']}, "
                    f"{each_expense['category']}, "
                    f"{each_expense['description']}, "
                    f"{each_expense['amount']}"
                )
                count += 1

    elif choice == "3":
        total = 0

        for each_expense in expenseslist:
            total += each_expense["amount"]

        print("\nTotal expenses =", total)

    elif choice == "4":
        print("Thanks for visiting the app.")
        break

    else:
        print("Invalid choice.")


                              
        