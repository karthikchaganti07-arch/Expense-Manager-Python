import os
import json
class ExpenseManager:
    def __init__(self):
        self.filename = os.path.join(os.path.dirname(__file__), "expenses.json")
        self.expenses = self.load_from_file()

    def load_from_file(self):
         try:
            with open(self.filename, "r") as f:
                return json.load(f)
         except FileNotFoundError:
            return []
         except json.JSONDecodeError:
            print("⚠ File corrupted. Starting fresh.")
            return []

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump(self.expenses, f, indent=4)


    def show_menu(self):
        print("\n--- Expense Manager ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Edit Expense")
        print("7. Exit")

    def add_expense(self):
        print("\nAdd Expense")
        while True:
            amt = input("Enter amount: ")
            try:
                amount = float(amt)
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Enter a number.")

        category = input("Enter category: ").strip().lower()
        description = input("Enter description: ").strip()

        # Generate unique ID
        new_id = max([e["id"] for e in self.expenses], default=0) + 1

        self.expenses.append({
            "id": new_id,
            "amount": amount,
            "category": category,
            "description": description
        })
        print("Expense added successfully!")

    def view_expenses(self):
        print("\nView Expenses")
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        for e in self.expenses:
            print(f"{e['id']} | ₹{e['amount']} | {e['category']} | {e['description']}")
        print("-" * 40)

    def total_expense(self):
        print("\nTotal Expense")
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        total = sum(e['amount'] for e in self.expenses)
        print(f"Total Expense: ₹{total}")

    def search_expense(self):
        print("\nSearch Expense")
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        search = input("Enter category: ").strip().lower()
        found = False
        for e in self.expenses:
            if search in e["category"]:
                print(f"{e['id']} | ₹{e['amount']} | {e['category']} | {e['description']}")
                found = True

        if not found:
            print("No expenses found in this category.")

    def delete_expense(self):
        if not self.expenses:
            print("No expenses to delete.")
            return
        try:
            eid = int(input("Enter Expense ID to delete: "))
        except ValueError:
            print("Invalid ID.")
            return

        for e in self.expenses:
            if e["id"] == eid:
                self.expenses.remove(e)
                print("Expense deleted successfully.")
                return
        print("Expense ID not found.")

    def edit_expense(self):
        if not self.expenses:
            print("No expenses to edit.")
            return
        try:
            eid = int(input("Enter Expense ID to edit: "))
        except ValueError:
            print("Invalid ID.")
            return

        for e in self.expenses:
            if e["id"] == eid:
                print("Leave blank to keep old value.")

                amt = input(f"New amount ({e['amount']}): ").strip()
                if amt:
                    try:
                        e["amount"] = float(amt)
                    except ValueError:
                        print("Invalid amount. Keeping old value.")

                cat = input(f"New category ({e['category']}): ").strip()
                if cat:
                    e["category"] = cat.lower()

                desc = input(f"New description ({e['description']}): ").strip()
                if desc:
                    e["description"] = desc

                print("Expense updated successfully.")
                return
        print("Expense ID not found.")

    def run(self):
        while True:
            self.show_menu()
            choice = input(f"Enter your choice (1-7): ").strip()
            if not choice.isdigit():
                print("Invalid input.")
                continue

            choice = int(choice)
            if choice == 1:
                self.add_expense()
            elif choice == 2:
                self.view_expenses()
            elif choice == 3:
                self.total_expense()
            elif choice == 4:
                self.search_expense()
            elif choice == 5:
                self.delete_expense()
            elif choice == 6:
                self.edit_expense()
            elif choice == 7:
                self.save_to_file()
                print("Data saved. Goodbye!")
                break
            else:
                print("Choice must be between 1 and 7.")


# Run the program
if __name__ == "__main__":
    manager = ExpenseManager()
    manager.run()
