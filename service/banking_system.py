"""
Banking System Manager
Central system to manage all accounts and operations
Demonstrates: Polymorphism, Encapsulation
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model import Account, SavingsAccount, CurrentAccount, Customer
from typing import Dict, Optional


class BankingSystem:
    """
    Banking System Manager - handles all account operations
    Demonstrates POLYMORPHISM - works with Account interface
    """
    
    def __init__(self):
        """Initialize the banking system"""
        self._accounts: Dict[str, Account] = {}
        self._customers: Dict[str, Customer] = {}
        self._account_counter = 1000
        self._customer_counter = 100
    
    def _generate_account_number(self) -> str:
        """Generate unique account number"""
        self._account_counter += 1
        return f"ACC{self._account_counter}"
    
    def _generate_customer_id(self) -> str:
        """Generate unique customer ID"""
        self._customer_counter += 1
        return f"CUST{self._customer_counter}"
    
    def create_customer(self, name: str, email: str, phone_number: str, 
                       address: str) -> Customer:
        """
        Create a new customer
        
        Args:
            name: Customer name
            email: Customer email
            phone_number: Customer phone
            address: Customer address
            
        Returns:
            Customer: Created customer object
        """
        customer_id = self._generate_customer_id()
        customer = Customer(customer_id, name, email, phone_number, address)
        self._customers[customer_id] = customer
        print(f"Customer created successfully! Customer ID: {customer_id}")
        return customer
    
    def create_savings_account(self, account_holder_name: str, 
                              initial_balance: float) -> Optional[Account]:
        """
        Create a Savings Account
        Demonstrates POLYMORPHISM - returns Account type
        
        Args:
            account_holder_name: Name of account holder
            initial_balance: Initial deposit amount
            
        Returns:
            Account: Created savings account or None if error
        """
        try:
            account_number = self._generate_account_number()
            account = SavingsAccount(account_number, account_holder_name, 
                                    initial_balance)
            self._accounts[account_number] = account
            
            print("\n✓ Savings Account created successfully!")
            print(f"Account Number: {account_number}")
            print(f"Account Holder: {account_holder_name}")
            print(f"Initial Balance: ₹{initial_balance:.2f}")
            
            return account
        except ValueError as e:
            print(f"Error creating account: {e}")
            return None
    
    def create_current_account(self, account_holder_name: str, 
                              initial_balance: float) -> Optional[Account]:
        """
        Create a Current Account
        Demonstrates POLYMORPHISM - returns Account type
        
        Args:
            account_holder_name: Name of account holder
            initial_balance: Initial deposit amount
            
        Returns:
            Account: Created current account or None if error
        """
        try:
            account_number = self._generate_account_number()
            account = CurrentAccount(account_number, account_holder_name, 
                                    initial_balance)
            self._accounts[account_number] = account
            
            print("\n✓ Current Account created successfully!")
            print(f"Account Number: {account_number}")
            print(f"Account Holder: {account_holder_name}")
            print(f"Initial Balance: ₹{initial_balance:.2f}")
            
            return account
        except ValueError as e:
            print(f"Error creating account: {e}")
            return None
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """
        Get account by account number
        
        Args:
            account_number: Account number to retrieve
            
        Returns:
            Account: Account object or None if not found
        """
        return self._accounts.get(account_number)
    
    def deposit(self, account_number: str, amount: float):
        """
        Deposit money into an account
        Demonstrates POLYMORPHISM - calls appropriate deposit method
        
        Args:
            account_number: Target account number
            amount: Amount to deposit
        """
        account = self._accounts.get(account_number)
        if account is None:
            print("Account not found!")
            return
        
        try:
            account.deposit(amount)  # Polymorphic call
        except ValueError as e:
            print(f"Error: {e}")
    
    def withdraw(self, account_number: str, amount: float):
        """
        Withdraw money from an account
        Demonstrates POLYMORPHISM - different behavior for Savings vs Current
        
        Args:
            account_number: Source account number
            amount: Amount to withdraw
        """
        account = self._accounts.get(account_number)
        if account is None:
            print("Account not found!")
            return
        
        account.withdraw(amount)  # Polymorphic call
    
    def check_balance(self, account_number: str):
        """
        Check account balance
        
        Args:
            account_number: Account number to check
        """
        account = self._accounts.get(account_number)
        if account is None:
            print("Account not found!")
            return
        
        print("\n========== Balance Inquiry ==========")
        print(f"Account Number: {account_number}")
        print(f"Account Holder: {account.get_account_holder_name()}")
        print(f"Current Balance: ₹{account.get_balance():.2f}")
        print("====================================\n")
    
    def display_account_info(self, account_number: str):
        """
        Display detailed account information
        Demonstrates POLYMORPHISM - different info for different account types
        
        Args:
            account_number: Account number to display
        """
        account = self._accounts.get(account_number)
        if account is None:
            print("Account not found!")
            return
        
        # Polymorphic call
        account.display_account_info()
        
        # Display specific details based on account type
        if isinstance(account, SavingsAccount):
            account.display_savings_account_details()
        elif isinstance(account, CurrentAccount):
            account.display_current_account_details()
    
    def display_transaction_history(self, account_number: str):
        """
        Display transaction history
        
        Args:
            account_number: Account number to display history for
        """
        account = self._accounts.get(account_number)
        if account is None:
            print("Account not found!")
            return
        
        account.display_transaction_history()
    
    def apply_monthly_charges(self, account_number: str):
        """
        Apply monthly charges/interest to an account
        Demonstrates POLYMORPHISM - different behavior for Savings vs Current
        
        Args:
            account_number: Account number to apply charges to
        """
        account = self._accounts.get(account_number)
        if account is None:
            print("Account not found!")
            return
        
        # Polymorphic call
        account.apply_monthly_charges()
    
    def apply_monthly_charges_to_all(self):
        """Apply monthly charges to all accounts"""
        print("\n========== Applying Monthly Charges/Interest to All Accounts ==========")
        for account in self._accounts.values():
            print(f"\nProcessing: {account.get_account_number()} - "
                  f"{account.get_account_holder_name()}")
            account.apply_monthly_charges()  # Polymorphic call
        print("\n======================================================================\n")
    
    def transfer_funds(self, from_account_number: str, to_account_number: str, 
                      amount: float):
        """
        Transfer money between accounts
        
        Args:
            from_account_number: Source account number
            to_account_number: Destination account number
            amount: Amount to transfer
        """
        from_account = self._accounts.get(from_account_number)
        to_account = self._accounts.get(to_account_number)
        
        if from_account is None or to_account is None:
            print("One or both accounts not found!")
            return
        
        if amount <= 0:
            print("Transfer amount must be positive!")
            return
        
        print("\n========== Fund Transfer ==========")
        print(f"From: {from_account_number} ({from_account.get_account_holder_name()})")
        print(f"To: {to_account_number} ({to_account.get_account_holder_name()})")
        print(f"Amount: ₹{amount:.2f}")
        
        # Attempt withdrawal from source account
        if from_account.withdraw(amount):
            # If successful, deposit to destination account
            try:
                to_account.deposit(amount)
                print("\n✓ Transfer completed successfully!")
            except Exception as e:
                # If deposit fails, refund the withdrawn amount
                from_account.deposit(amount)
                print(f"Transfer failed: {e}")
        else:
            print("\nTransfer failed due to insufficient funds.")
        
        print("===================================\n")
    
    def list_all_accounts(self):
        """List all accounts in the system"""
        if not self._accounts:
            print("No accounts in the system.")
            return
        
        print("\n========== All Bank Accounts ==========")
        for account in self._accounts.values():
            print(f"{account.get_account_number():<12} | "
                  f"{account.get_account_holder_name():<20} | "
                  f"{account.get_account_type():<18} | "
                  f"Balance: ₹{account.get_balance():<10.2f}")
        print("=======================================\n")
    
    def get_total_accounts(self) -> int:
        """Get total number of accounts"""
        return len(self._accounts)
    
    def account_exists(self, account_number: str) -> bool:
        """
        Check if account exists
        
        Args:
            account_number: Account number to check
            
        Returns:
            bool: True if account exists, False otherwise
        """
        return account_number in self._accounts
