import datetime

customers = {
    "avi cohen": {"name": "Avi Cohen", "pin": "1234", "balance": 1000},
    "yossi cohen": {"name": "Yossi Cohen", "pin": "6543", "balance": 500},
    "yuri levi": {"name": "Yuri Levi", "pin": "5852", "balance": 800},
}

def login():
    print("\n__Welcome to the ATM__")
    name = input("Enter your name: ").strip().lower()
    
    if name not in customers:
        print("Invalid name. Please try again.")
        return None
        
    print(f"Welcome to {customers[name]['name']}")
    
    attempts = 3
    for i in range(attempts):
        pin = input(f"Enter your PIN code (Attempts left: {attempts - i}): ")
        
        if customers[name]["pin"] == pin:
            return customers[name]
        else:
            if i < attempts - 1:
                print("Invalid PIN. Please try again.")
            else:
                print("Invalid PIN. You have exceeded the maximum number of attempts.")
                
    return None

def handle_withdrawal(customer):
    while True:
        print("\n--- Quick Withdrawal Menu ---")
        print("1. Withdraw 50 NIS")
        print("2. Withdraw 100 NIS")
        print("3. Withdraw 200 NIS")
        print("4. Withdraw 500 NIS")
        print("5. Enter custom amount")
        print("6. Cancel and return to main menu")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            amount = 50
        elif choice == '2':
            amount = 100
        elif choice == '3':
            amount = 200
        elif choice == '4':
            amount = 500
        elif choice == '5':
            try:
                amount = int(input("Enter custom amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be positive. Please try again.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
        elif choice == '6':
            print("Withdrawal canceled.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")
            continue
            
        if amount > customer["balance"]:
            print("sorry, operation could not happen, you don't have enough Balance for this operation")
            continue
            
        customer["balance"] -= amount
        print("OK")
        print(f"Successfully withdrew {amount} NIS.")
        print(f"Your new balance is {customer['balance']} NIS.")
        break

def handle_deposit(customer):
    while True:
        try:
            amount = int(input("How much would you like to Deposit? (0 to cancel): "))
            
            if amount == 0:
                print("Deposit canceled.")
                break
            
            if amount < 20:
                print("Minimum deposit is 20 NIS. Please try again.")
                continue
                
            if amount % 10 != 0 or amount == 30:
                print("Invalid amount! Deposit must be in valid banknotes (20, 50, 100, 200 NIS).")
                continue
            
            customer["balance"] += amount
            print("OK")
            print(f"Successfully deposited {amount} NIS.")
            print(f"Your new balance is {customer['balance']} NIS.")
            break
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def change_pin(customer):
    while True:
        new_pin = input("Enter your new 4-digit PIN code: ").strip()
        
        # בדיקה שהקוד מורכב מ-4 ספרות
        if len(new_pin) == 4 and new_pin.isdigit():
            # השדרוג המתוחכם: חסימת שימוש באותו קוד נוכחי
            if new_pin == customer["pin"]:
                print("New PIN cannot be the same as your current PIN. Please choose a different code.")
                continue
                
            customer["pin"] = new_pin
            print("OK! PIN code changed successfully.")
            break
        else:
            print("Invalid PIN! Code must be exactly 4 digits.")

def print_recipe(customer):
    current_time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    print("\n\"\"\"")
    print(f"Hello {customer['name']},")
    print(f"At this moment DATE: {current_time} you got {customer['balance']} NIS in your account")
    print("Thank you for using your ATM")
    print("\"\"\"")

def atm_menu(customer):
    while True:
        print("\n=== ATM MENU ===")
        print("Press button d to Deposit Money")
        print("Press button w to Withdraw Money")
        print("Press button c to Check your Balance")
        print("Press button p to change PIN_CODE")
        print("Press button r to create RECIPE")
        print("Press button q to Quit")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'c':
            print(f"Your current Balance is {customer['balance']} NIS")
        elif choice == 'd':
            handle_deposit(customer)
        elif choice == 'w':
            handle_withdrawal(customer)
        elif choice == 'p':
            change_pin(customer)
        elif choice == 'r':
            print_recipe(customer)
        elif choice == 'q':
            print(f"GOODBYE {customer['name'].upper()}, HAVE A NICE DAY")
            return True
        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        customer = login()
        if customer:
            if atm_menu(customer):
                continue
            
        while True:
            another_user = input("\nWould you like to try again / sign in? (y/n): ").strip().lower()
            if another_user == 'y':
                break
            elif another_user == 'n':
                print("Shutting down ATM. Goodbye!")
                return
            else:
                print("Invalid input! Please enter 'y' for Yes or 'n' for No.")

if __name__ == "__main__":
    main()