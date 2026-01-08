"""
Banking Application - Main Entry Point
Console-based Banking System with menu-driven interface
"""

import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from service.banking_system import BankingSystem


class BankingApp:
    """Main application class for banking system"""
    
    def __init__(self):
        """Initialize the banking application"""
        self.banking_system = BankingSystem()
    
    def display_main_menu(self):
        """Display the main menu"""
        print("\n╔═══════════════════════════════════════════════════════╗")
        print("║              MAIN MENU                                ║")
        print("╠═══════════════════════════════════════════════════════╣")
        print("║  1. Create New Account                                ║")
        print("║  2. Deposit Money                                     ║")
        print("║  3. Withdraw Money                                    ║")
        print("║  4. Check Balance                                     ║")
        print("║  5. View Account Details                              ║")
        print("║  6. View Transaction History                          ║")
        print("║  7. Transfer Funds                                    ║")
        print("║  8. Apply Monthly Charges/Interest                    ║")
        print("║  9. List All Accounts                                 ║")
        print("║  0. Exit                                              ║")
        print("╚═══════════════════════════════════════════════════════╝")
    
    def get_int_input(self, prompt: str) -> int:
        
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    def get_float_input(self, prompt: str) -> float:
       
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
    
    def create_account_menu(self):
        """Menu for creating new accounts"""
        print("\n========== Create New Account ==========")
        print("1. Savings Account")
        print("2. Current Account")
        print("========================================")
        
        account_type = self.get_int_input("Select account type: ")
        
        name = input("Enter account holder name: ")
        initial_balance = self.get_float_input("Enter initial deposit amount: ₹")
        
        if account_type == 1:
            print("\n--- Savings Account Requirements ---")
            print("• Minimum Balance: ₹1000")
            print("• Interest Rate: 4.5% per annum")
            print("• Free Withdrawals: 5 per month")
            print("• Withdrawal Limit: ₹50,000")
            account = self.banking_system.create_savings_account(name, initial_balance)
        elif account_type == 2:
            print("\n--- Current Account Requirements ---")
            print("• Minimum Balance: ₹5000")
            print("• Overdraft Limit: ₹50,000")
            print("• Monthly Maintenance Fee: ₹100")
            account = self.banking_system.create_current_account(name, initial_balance)
        else:
            print("Invalid account type!")
            return
        
        if account is not None:
            print("\n✓ Please note your Account Number for future transactions.")
    
    def deposit_money(self):
        """Menu for depositing money"""
        print("\n========== Deposit Money ==========")
        account_number = input("Enter account number: ")
        
        if not self.banking_system.account_exists(account_number):
            print("Account not found!")
            return
        
        amount = self.get_float_input("Enter deposit amount: ₹")
        self.banking_system.deposit(account_number, amount)
    
    def withdraw_money(self):
        """Menu for withdrawing money"""
        print("\n========== Withdraw Money ==========")
        account_number = input("Enter account number: ")
        
        if not self.banking_system.account_exists(account_number):
            print("Account not found!")
            return
        
        amount = self.get_float_input("Enter withdrawal amount: ₹")
        self.banking_system.withdraw(account_number, amount)
    
    def check_balance(self):
        """Menu for checking balance"""
        print("\n========== Balance Inquiry ==========")
        account_number = input("Enter account number: ")
        
        self.banking_system.check_balance(account_number)
    
    def view_account_details(self):
        """Menu for viewing account details"""
        print("\n========== Account Details ==========")
        account_number = input("Enter account number: ")
        
        self.banking_system.display_account_info(account_number)
    
    def view_transaction_history(self):
        """Menu for viewing transaction history"""
        print("\n========== Transaction History ==========")
        account_number = input("Enter account number: ")
        
        self.banking_system.display_transaction_history(account_number)
    
    def transfer_funds(self):
        """Menu for transferring funds"""
        print("\n========== Transfer Funds ==========")
        from_account = input("Enter source account number: ")
        
        if not self.banking_system.account_exists(from_account):
            print("Source account not found!")
            return
        
        to_account = input("Enter destination account number: ")
        
        if not self.banking_system.account_exists(to_account):
            print("Destination account not found!")
            return
        
        amount = self.get_float_input("Enter transfer amount: ₹")
        self.banking_system.transfer_funds(from_account, to_account, amount)
    
    def apply_monthly_charges(self):
        """Menu for applying monthly charges"""
        print("\n========== Monthly Charges/Interest ==========")
        print("1. Apply to specific account")
        print("2. Apply to all accounts")
        
        choice = self.get_int_input("Enter your choice: ")
        
        if choice == 1:
            account_number = input("Enter account number: ")
            self.banking_system.apply_monthly_charges(account_number)
        elif choice == 2:
            self.banking_system.apply_monthly_charges_to_all()
        else:
            print("Invalid choice!")
    
    def list_all_accounts(self):
        """List all accounts"""
        self.banking_system.list_all_accounts()
    
    def run(self):
        """Main application loop"""
        print("\n╔═══════════════════════════════════════════════════════╗")
        print("║     WELCOME TO PYTHON BANKING SYSTEM                 ║")
        print("║     Console-Based Banking Application                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        
        running = True
        
        while running:
            self.display_main_menu()
            choice = self.get_int_input("Enter your choice: ")
            
            if choice == 1:
                self.create_account_menu()
            elif choice == 2:
                self.deposit_money()
            elif choice == 3:
                self.withdraw_money()
            elif choice == 4:
                self.check_balance()
            elif choice == 5:
                self.view_account_details()
            elif choice == 6:
                self.view_transaction_history()
            elif choice == 7:
                self.transfer_funds()
            elif choice == 8:
                self.apply_monthly_charges()
            elif choice == 9:
                self.list_all_accounts()
            elif choice == 0:
                print("\n╔═══════════════════════════════════════════════════════╗")
                print("║  Thank you for using Python Banking System!          ║")
                print("║  Have a great day!                                    ║")
                print("╚═══════════════════════════════════════════════════════╝\n")
                running = False
            else:
                print("Invalid choice! Please try again.")
            
            if running:
                input("\nPress Enter to continue...")


def main():
    """Main entry point"""
    app = BankingApp()
    app.run()


if __name__ == "__main__":
    main()
