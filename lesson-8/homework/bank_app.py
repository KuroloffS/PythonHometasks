import json
import os
import sys

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        account_number = len(self.accounts) + 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        account.balance += amount
        self.save_to_file()
        print(f"Deposited {amount}. New balance: {account.balance}")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > account.balance:
            print("Insufficient balance.")
            return

        account.balance -= amount
        self.save_to_file()
        print(f"Withdrew {amount}. New balance: {account.balance}")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            json.dump(data, file)

    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            try:
                with open("accounts.txt", "r") as file:
                    data = json.load(file)
                    self.accounts = {int(acc_num): Account.from_dict(acc) for acc_num, acc in data.items()}
            except (json.JSONDecodeError, ValueError) as e:
                print("Error loading account data. The file might be corrupted.")
                self.accounts = {}

# Main program
if __name__ == "__main__":
    bank = Bank()
    try:
        while True:
            print("\n1. Create Account")
            print("2. View Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter your name: ")
                try:
                    initial_deposit = float(input("Enter initial deposit: "))
                    bank.create_account(name, initial_deposit)
                except ValueError as e:
                    print(e)

            elif choice == "2":
                try:
                    account_number = int(input("Enter account number: "))
                    bank.view_account(account_number)
                except ValueError:
                    print("Invalid account number.")

            elif choice == "3":
                try:
                    account_number = int(input("Enter account number: "))
                    amount = float(input("Enter deposit amount: "))
                    bank.deposit(account_number, amount)
                except ValueError:
                    print("Invalid input.")

            elif choice == "4":
                try:
                    account_number = int(input("Enter account number: "))
                    amount = float(input("Enter withdrawal amount: "))
                    bank.withdraw(account_number, amount)
                except ValueError:
                    print("Invalid input.")

            elif choice == "5":
                print("Thank you for using the bank application!")
                break

            else:
                print("Invalid choice. Please try again.")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting safely...")
        sys.exit(0)
