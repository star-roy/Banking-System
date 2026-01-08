"""
Account Base Class (Abstract)
Demonstrates Abstraction and Encapsulation
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from .transaction import Transaction


class Account(ABC):
    """
    Abstract base class for all account types
    Demonstrates ABSTRACTION - defines contract that all accounts must follow
    Demonstrates ENCAPSULATION - private fields with controlled access
    
    Attributes:
        _account_number (str): Unique account number
        _account_holder_name (str): Name of account holder
        _balance (float): Current account balance
        _created_date (datetime): When account was created
        _transaction_history (List[Transaction]): List of all transactions
    """
    
    def __init__(self, account_number: str, account_holder_name: str, 
                 initial_balance: float):
        """
        Initialize a new account
        
        Args:
            account_number: Unique account identifier
            account_holder_name: Name of account holder
            initial_balance: Initial deposit amount
        """
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._balance = initial_balance
        self._created_date = datetime.now()
        self._transaction_history: List[Transaction] = []
        
        # Record initial deposit
        if initial_balance > 0:
            self._transaction_history.append(
                Transaction("DEPOSIT", initial_balance, "Initial Deposit")
            )
    
    # Getter methods (Encapsulation - controlled access to private fields)
    def get_account_number(self) -> str:
        """Get account number"""
        return self._account_number
    
    def get_account_holder_name(self) -> str:
        """Get account holder name"""
        return self._account_holder_name
    
    def get_balance(self) -> float:
        """Get current balance"""
        return self._balance
    
    def get_created_date(self) -> datetime:
        """Get account creation date"""
        return self._created_date
    
    def get_transaction_history(self) -> List[Transaction]:
        """Get copy of transaction history"""
        return self._transaction_history.copy()
    
    # Protected setter - accessible to subclasses
    def _set_balance(self, balance: float):
        """Set balance (protected - for subclass use)"""
        self._balance = balance
    
    def deposit(self, amount: float):
        """
        Deposit money into account
        
        Args:
            amount: Amount to deposit
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._transaction_history.append(
            Transaction("DEPOSIT", amount, "Cash Deposit")
        )
        print(f"Deposit successful! Amount: ₹{amount:.2f}")
    
    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from account (ABSTRACT METHOD)
        Must be implemented by subclasses with specific rules
        
        Args:
            amount: Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        pass
    
    @abstractmethod
    def apply_monthly_charges(self):
        """
        Apply monthly charges/interest (ABSTRACT METHOD)
        Must be implemented by subclasses with specific rules
        """
        pass
    
    @abstractmethod
    def get_account_type(self) -> str:
        """
        Get account type (ABSTRACT METHOD)
        Must be implemented by subclasses
        
        Returns:
            str: Account type name
        """
        pass
    
    def display_account_info(self):
        """Display basic account information"""
        print("\n========== Account Information ==========")
        print(f"Account Type: {self.get_account_type()}")
        print(f"Account Number: {self._account_number}")
        print(f"Account Holder: {self._account_holder_name}")
        print(f"Current Balance: ₹{self._balance:.2f}")
        print(f"Account Created: {self._created_date.strftime('%Y-%m-%d')}")
        print("=========================================\n")
    
    def display_transaction_history(self):
        """Display complete transaction history"""
        print("\n========== Transaction History ==========")
        print(f"Account: {self._account_number} ({self._account_holder_name})")
        print("-----------------------------------------")
        
        if not self._transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self._transaction_history:
                print(transaction)
        
        print("=========================================\n")
    
    def _add_transaction(self, transaction_type: str, amount: float, 
                        description: str):
        """
        Add transaction to history (protected method for subclasses)
        
        Args:
            transaction_type: Type of transaction
            amount: Transaction amount
            description: Transaction description
        """
        self._transaction_history.append(
            Transaction(transaction_type, amount, description)
        )
