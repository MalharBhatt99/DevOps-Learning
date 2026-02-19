# 🏦 Banking System CLI

A simple console-based banking system designed to simulate core banking operations without a graphical user interface.

This project focuses on backend logic, object-oriented design, and clean system structuring.

---

# 📌 Project Objective

Build a minimal banking engine that allows users to:

1. Create an account
2. Deposit money
3. Withdraw money
4. Check balance
5. Exit the system

The system operates entirely in memory (no database).

---

# 🎯 Functional Requirements

## 1️⃣ Create Account
- User provides:
  - Name
  - Initial deposit amount
- System generates:
  - Unique account number
- Initial deposit must not be negative.

---

## 2️⃣ Deposit Money
- User provides:
  - Account number
  - Deposit amount
- System:
  - Verifies account exists
  - Verifies deposit amount is positive
  - Updates balance

---

## 3️⃣ Withdraw Money
- User provides:
  - Account number
  - Withdrawal amount
- System:
  - Verifies account exists
  - Verifies withdrawal amount is positive
  - Checks sufficient balance
  - Deducts amount if valid

---

## 4️⃣ Check Balance
- User provides:
  - Account number
- System:
  - Verifies account exists
  - Displays current balance

---

## 5️⃣ Exit
- Terminates application safely.

---

# 🏗 System Design

## 🔹 Architecture Type

Monolithic CLI application with object-oriented structure.

The system consists of:

- Account Entity
- BankingSystem Controller
- Main Application (Menu Loop)

---

# 🧠 Core Components

## 1️⃣ Account Class

### Responsibilities:
- Store account data
- Handle deposit logic
- Handle withdrawal logic
- Maintain balance integrity

### Attributes:
- accountNumber
- accountHolderName
- balance

### Methods:
- deposit(amount)
- withdraw(amount)
- getBalance()
- getAccountDetails()

Encapsulation principle:  
Balance should only be modified through Account methods.

---

## 2️⃣ BankingSystem Class

### Responsibilities:
- Store all accounts
- Generate unique account numbers
- Locate account by account number
- Coordinate operations

### Internal Storage:
Use a Map / Dictionary:

Key → accountNumber  
Value → Account object  

Reason:
Efficient lookup (O(1) time complexity)

### Additional Attributes:
- nextAccountNumber (auto-increment strategy)

---

## 3️⃣ Main Class

### Responsibilities:
- Display menu
- Accept user input
- Call BankingSystem methods
- Maintain program loop

---

# 🔁 Application Flow

1. Start Program
2. Display Menu
3. Accept User Choice
4. Execute Selected Operation
5. Return to Menu
6. Repeat until Exit

---

# 🛡 Validation Rules

## Account Creation
- Name must not be empty
- Initial deposit ≥ 0

## Deposit
- Account must exist
- Amount > 0

## Withdrawal
- Account must exist
- Amount > 0
- Amount ≤ current balance

## Balance Check
- Account must exist

---

# ⚙ Data Structure Decision

Accounts are stored using:
```bash
Map<Integer, Account>
```

Why?
- Fast lookup by account number
- Clean separation of data
- Scalable design

---

# 🧪 Edge Cases to Handle

- Invalid account number
- Negative deposit amount
- Withdrawal greater than balance
- Non-numeric input
- No accounts created yet
- Empty input

Handling edge cases increases system robustness.

---

# 📂 Suggested Project Structure

```bash
banking-system-cli/
│
├── src/
│   ├── Account
│   ├── BankingSystem
│   └── Main
│
├── README.md
└── notes.md
```

---

# 🚀 Development Roadmap

## Phase 1 – Basic Functionality
- Implement Account class
- Implement BankingSystem class
- Implement menu loop
- Add basic validation

## Phase 2 – Improvements
- Add transaction history
- Add timestamps
- Improve input validation
- Add formatted output

## Phase 3 – Persistence
- Store accounts in file
- Load accounts on startup
- Save data before exit

## Phase 4 – Advanced Upgrade
- Convert to REST API
- Add database integration
- Add authentication
- Dockerize application

---

# 📊 System Design Principles Applied

- Object-Oriented Programming
- Encapsulation
- Separation of Concerns
- Single Responsibility Principle
- Data Structure Optimization

---

# 💡 Learning Goals

This project helps practice:

- OOP design
- Clean architecture thinking
- Input validation
- Error handling
- Data structure selection
- Backend logic structuring

---

# ⚡ Philosophy

Build small systems.  
Design cleanly.  
Validate thoroughly.  
Improve iteratively.

---

# 📌 Notes

This is a learning-focused project.  
The system runs in-memory and does not persist data between executions (unless extended).

Future improvements are encouraged.

---

🏦 Built for backend logic mastery.
