"""
Transaction Class
Records all banking transactions with timestamp
"""

from datetime import datetime


class Transaction:
    """
    Represents a single banking transaction
    
    Attributes:
        type (str): Transaction type (DEPOSIT, WITHDRAWAL, CHARGES, INTEREST)
        amount (float): Transaction amount
        description (str): Transaction description
        timestamp (datetime): When the transaction occurred
    """
    
    def __init__(self, transaction_type: str, amount: float, description: str):
        """
        Initialize a new transaction
        
        Args:
            transaction_type: Type of transaction
            amount: Transaction amount
            description: Description of the transaction
        """
        self.type = transaction_type
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()
    
    def get_type(self) -> str:
        """Get transaction type"""
        return self.type
    
    def get_amount(self) -> float:
        """Get transaction amount"""
        return self.amount
    
    def get_description(self) -> str:
        """Get transaction description"""
        return self.description
    
    def get_timestamp(self) -> datetime:
        """Get transaction timestamp"""
        return self.timestamp
    
    def __str__(self) -> str:
        """String representation of transaction"""
        formatted_time = self.timestamp.strftime("%d-%m-%Y %H:%M:%S")
        return f"[{formatted_time}] {self.type:<12} ₹{self.amount:<10.2f} - {self.description}"
