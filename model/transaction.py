"""
Transaction Class
Records all banking transactions with timestamp
"""

from datetime import datetime


class Transaction:
    def __init__(self, transaction_type: str, amount: float, description: str):
        
        self.type = transaction_type
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()
    
    def get_type(self) -> str:
        return self.type
    
    def get_amount(self) -> float:
        return self.amount
    
    def get_description(self) -> str:
        return self.description
    
    def get_timestamp(self) -> datetime:
        return self.timestamp
    
    def __str__(self) -> str:
        """String representation of transaction"""
        formatted_time = self.timestamp.strftime("%d-%m-%Y %H:%M:%S")
        return f"[{formatted_time}] {self.type:<12} ₹{self.amount:<10.2f} - {self.description}"
