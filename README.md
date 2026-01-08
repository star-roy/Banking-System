# Python Banking System

A console-based Banking System application built in Python3, demonstrating core Object-Oriented Programming (OOP) principles including **Abstraction**, **Inheritance**, **Encapsulation**, and **Polymorphism**.

## 🎯 Project Overview

This project implements a fully functional banking system with support for multiple account types, transaction management, and interactive user operations. It's a Python3 port of the Java Banking System, designed to showcase clean, reusable, and scalable code architecture.

## 🛠️ Tech Stack

- **Language**: Python 3.8 or higher
- **Concepts**: Object-Oriented Programming (OOP)
- **Architecture**: Console-based application with menu-driven interface
- **Standard Library**: Uses Python's built-in modules (abc, datetime, typing)

## ✨ Features

### Account Types
1. **Savings Account**
   - Minimum balance requirement: ₹1,000
   - Interest rate: 4.5% per annum
   - 5 free withdrawals per month
   - Withdrawal limit: ₹50,000 per transaction
   - Additional charges after free withdrawal limit

2. **Current Account**
   - Minimum balance requirement: ₹5,000
   - Overdraft facility: Up to ₹50,000
   - Monthly maintenance fee: ₹100
   - Overdraft interest: 12% per annum
   - No withdrawal limits

### Banking Operations
- ✅ Create new accounts (Savings/Current)
- ✅ Deposit money
- ✅ Withdraw money (with account-specific rules)
- ✅ Check account balance
- ✅ View detailed account information
- ✅ View complete transaction history
- ✅ Transfer funds between accounts
- ✅ Apply monthly charges/interest
- ✅ List all accounts in the system

## 🏗️ Project Structure

```
Banking System Python/
│
├── banking_app.py              # Main application with menu
├── model/
│   ├── __init__.py            # Package initializer
│   ├── account.py             # Abstract base class
│   ├── savings_account.py     # Savings account implementation
│   ├── current_account.py     # Current account implementation
│   ├── customer.py            # Customer information
│   └── transaction.py         # Transaction records
├── service/
│   ├── __init__.py            # Package initializer
│   └── banking_system.py      # Banking system manager
├── README.md
└── requirements.txt
```

## 🎓 OOP Concepts Demonstrated

### 1. **Abstraction**
- `Account` is an abstract base class (ABC) that defines the contract for all account types
- Abstract methods like `withdraw()`, `apply_monthly_charges()`, and `get_account_type()` must be implemented by subclasses
- Uses Python's `abc` module to enforce abstraction
- Hides implementation details while exposing only necessary operations

### 2. **Inheritance**
- `SavingsAccount` and `CurrentAccount` extend the `Account` base class
- Inherit common properties (account_number, balance, account_holder_name)
- Inherit common methods (deposit, display_account_info, transaction history)
- Promotes code reusability and establishes "IS-A" relationships

### 3. **Encapsulation**
- Private fields (prefixed with `_`) with public getter methods for controlled access
- Protected setters (prefixed with `_`) accessible only to subclasses
- Data hiding ensures security and integrity
- Validation logic encapsulated within methods
- Property decorators can be used for Pythonic access patterns

### 4. **Polymorphism**
- **Method Overriding**: `withdraw()`, `apply_monthly_charges()` behave differently in Savings vs Current accounts
- **Runtime Polymorphism**: Same method call produces different results based on object type
- **Duck Typing**: Python's dynamic typing allows polymorphic behavior naturally
- **Collection of parent type**: `Dict[str, Account]` can hold both SavingsAccount and CurrentAccount objects
- Enables flexible and extensible code design

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher installed
- Command line terminal or IDE (VS Code, PyCharm, etc.)

### Using Command Line

1. **Navigate to the project directory**
   ```bash
   cd "d:\VISUALSTD\Banking System Python"
   ```

2. **Run the application**
   ```bash
   python banking_app.py
   ```

   Or on some systems:
   ```bash
   python3 banking_app.py
   ```

### Using VS Code

1. Open the folder in VS Code
2. Open `banking_app.py`
3. Press `F5` or click "Run" → "Run Without Debugging"
4. Or use the integrated terminal and run: `python banking_app.py`

## 📖 Usage Guide

### Creating an Account
1. Select option 1 from the main menu
2. Choose account type (Savings or Current)
3. Enter account holder name
4. Enter initial deposit (must meet minimum balance requirements)
5. Note the generated account number for future transactions

### Performing Transactions
- **Deposit**: Select option 2, enter account number and amount
- **Withdraw**: Select option 3, enter account number and amount (subject to account rules)
- **Check Balance**: Select option 4, enter account number
- **Transfer**: Select option 7, enter source and destination account numbers and amount

### Viewing Information
- **Account Details**: Select option 5 to see complete account information
- **Transaction History**: Select option 6 to view all transactions for an account
- **All Accounts**: Select option 9 to list all accounts in the system

### Monthly Processing
- Select option 8 to apply monthly charges/interest
- Choose to apply to a specific account or all accounts

## 🔑 Key Differences from Java Version

1. **Language Syntax**: Python's cleaner, more concise syntax
2. **Type Hints**: Uses Python's type hinting for better code clarity
3. **Abstract Base Classes**: Uses `abc` module instead of Java's abstract keyword
4. **Property Access**: Uses Pythonic getter/setter patterns with underscore prefix
5. **Exception Handling**: Uses Python's exception hierarchy
6. **String Formatting**: Uses f-strings and format() for cleaner output
7. **Collections**: Uses Python's built-in dict and list types

## 📝 Code Examples

### Creating Accounts (Polymorphism)
```python
# Banking system can work with Account interface
account1 = banking_system.create_savings_account("John Doe", 5000)
account2 = banking_system.create_current_account("Jane Smith", 10000)

# Both stored as Account type, but maintain their specific behavior
```

### Method Overriding (Polymorphism)
```python
# Same method call, different behavior
savings_account.withdraw(1000)  # Checks withdrawal count, applies charges if needed
current_account.withdraw(1000)  # May use overdraft facility

savings_account.apply_monthly_charges()  # Credits interest
current_account.apply_monthly_charges()  # Deducts maintenance fee
```

## 🧪 Testing the Application

Try these scenarios to see OOP principles in action:

1. **Test Inheritance**:
   - Create both Savings and Current accounts
   - Notice how both share common methods (deposit, display_account_info)
   - But have different behaviors for withdraw() and apply_monthly_charges()

2. **Test Polymorphism**:
   - Create multiple accounts of different types
   - Use "Apply to All Accounts" feature in monthly charges
   - See how the same method call behaves differently for each account type

3. **Test Encapsulation**:
   - Try to access account balance directly (you can't!)
   - All data access is controlled through methods
   - Validation ensures data integrity

4. **Test Abstraction**:
   - The Account class defines what operations are available
   - Implementation details are hidden in subclasses
   - You work with the Account interface, not concrete implementations

## 🎯 Learning Objectives

This project demonstrates:
- How to structure a Python application using OOP principles
- Proper use of abstract base classes and inheritance
- Implementing polymorphism for flexible, extensible code
- Encapsulation for data protection and integrity
- Clean code organization with packages and modules
- Console-based user interface design
- Transaction management and data persistence (in-memory)

## 🔄 Comparison with Java Version

| Aspect | Java | Python |
|--------|------|--------|
| **Abstraction** | `abstract` keyword | `ABC` and `@abstractmethod` |
| **Private Fields** | `private` keyword | `_` prefix convention |
| **Getters/Setters** | Explicit methods | Methods or `@property` decorator |
| **Type System** | Static typing | Dynamic with type hints |
| **Collections** | `Map<String, Account>` | `Dict[str, Account]` |
| **String Format** | `String.format()` | f-strings |
| **Exception** | Checked/Unchecked | All unchecked |
| **Import System** | `package`, `import` | Module-based imports |

## 🚀 Future Enhancements

Potential improvements:
- [ ] Add data persistence (JSON/SQLite database)
- [ ] Implement user authentication
- [ ] Add account statements (PDF generation)
- [ ] Implement interest calculation scheduler
- [ ] Add loan accounts
- [ ] Create web interface using Flask/Django
- [ ] Add unit tests using pytest
- [ ] Implement logging for audit trail
- [ ] Add multi-currency support
- [ ] Create REST API endpoints

## 📄 License

This project is created for educational purposes to demonstrate OOP concepts in Python.

## 👨‍💻 Author

Python implementation based on Java Banking System project.
Demonstrates OOP principles for BTech CSE portfolio.

## 🙏 Acknowledgments

- Original Java Banking System design
- Python ABC module documentation
- Object-Oriented Programming best practices

---

**Note**: This is a console-based educational project. For production banking applications, additional security measures, data persistence, and regulatory compliance features would be required.
