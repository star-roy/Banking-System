"""
Savings Account Class
Demonstrates INHERITANCE and POLYMORPHISM
"""

from .account import Account


class SavingsAccount(Account):
    """
    Savings Account with specific rules
    Demonstrates INHERITANCE - extends Account base class
    Demonstrates POLYMORPHISM - overrides abstract methods with savings-specific behavior
    
    Features:
        - Minimum balance requirement: ₹1,000
        - Interest rate: 4.5% per annum
        - 5 free withdrawals per month
        - Withdrawal limit: ₹50,000 per transaction
        - Additional charges after free withdrawal limit
    """
    
    # Class constants
    MINIMUM_BALANCE = 1000.0
    INTEREST_RATE = 4.5  # per annum
    WITHDRAWAL_LIMIT = 50000.0
    FREE_WITHDRAWALS = 5
    WITHDRAWAL_CHARGE = 10.0
    
    def __init__(self, account_number: str, account_holder_name: str, 
                 initial_balance: float):
        """
        Initialize a new Savings Account
        
        Args:
            account_number: Unique account identifier
            account_holder_name: Name of account holder
            initial_balance: Initial deposit amount
            
        Raises:
            ValueError: If initial balance is below minimum
        """
        if initial_balance < self.MINIMUM_BALANCE:
            raise ValueError(
                f"Initial balance must be at least ₹{self.MINIMUM_BALANCE} "
                f"for Savings Account"
            )
        
        super().__init__(account_number, account_holder_name, initial_balance)
        self._withdrawal_count = 0
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from savings account (POLYMORPHISM)
        Implements account-specific withdrawal rules
        
        Args:
            amount: Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        
        if amount > self.WITHDRAWAL_LIMIT:
            print(f"Withdrawal limit exceeded! Maximum allowed: ₹{self.WITHDRAWAL_LIMIT}")
            return False
        
        current_balance = self.get_balance()
        charge_amount = 0
        
        # Apply charge if free withdrawals exhausted
        if self._withdrawal_count >= self.FREE_WITHDRAWALS:
            charge_amount = self.WITHDRAWAL_CHARGE
            print(f"Note: Withdrawal charge of ₹{self.WITHDRAWAL_CHARGE} will be applied.")
        
        total_deduction = amount + charge_amount
        
        # Check minimum balance requirement
        if current_balance - total_deduction < self.MINIMUM_BALANCE:
            print(f"Insufficient balance! Minimum balance of ₹{self.MINIMUM_BALANCE} "
                  f"must be maintained.")
            return False
        
        # Process withdrawal
        self._set_balance(current_balance - total_deduction)
        self._add_transaction("WITHDRAWAL", amount, "Cash Withdrawal")
        
        if charge_amount > 0:
            self._add_transaction("CHARGES", charge_amount, "Withdrawal Charge")
        
        self._withdrawal_count += 1
        
        print(f"Withdrawal successful! Amount: ₹{amount:.2f}")
        if charge_amount > 0:
            print(f"Withdrawal charge: ₹{charge_amount:.2f}")
        print(f"Remaining Balance: ₹{self.get_balance():.2f}")
        
        return True
    
    def apply_monthly_charges(self):
        """
        Apply monthly interest (POLYMORPHISM)
        Credits interest and resets withdrawal count
        """
        current_balance = self.get_balance()
        monthly_interest = (current_balance * self.INTEREST_RATE) / (12 * 100)
        
        self._set_balance(current_balance + monthly_interest)
        self._add_transaction(
            "INTEREST", 
            monthly_interest, 
            f"Monthly Interest Credit @ {self.INTEREST_RATE}% p.a."
        )
        
        print(f"Monthly interest of ₹{monthly_interest:.2f} credited to account!")
        
        # Reset withdrawal count for new month
        self._withdrawal_count = 0
    
    def get_account_type(self) -> str:
        """
        Get account type (POLYMORPHISM)
        
        Returns:
            str: "Savings Account"
        """
        return "Savings Account"
    
    def display_savings_account_details(self):
        """Display detailed savings account information"""
        self.display_account_info()
        print(f"Interest Rate: {self.INTEREST_RATE}% per annum")
        print(f"Minimum Balance: ₹{self.MINIMUM_BALANCE}")
        print(f"Withdrawal Limit: ₹{self.WITHDRAWAL_LIMIT}")
        print(f"Free Withdrawals: {self.FREE_WITHDRAWALS} per month")
        print(f"Withdrawals this month: {self._withdrawal_count}")
    
    def get_interest_rate(self) -> float:
        """Get interest rate"""
        return self.INTEREST_RATE
    
    def get_minimum_balance(self) -> float:
        """Get minimum balance requirement"""
        return self.MINIMUM_BALANCE
    
    def get_withdrawal_count(self) -> int:
        """Get number of withdrawals this month"""
        return self._withdrawal_count
