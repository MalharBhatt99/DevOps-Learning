# 🏦 Banking System CLI

A simple console-based banking system designed to simulate core banking operations without a graphical user interface.

This project focuses on backend logic, object-oriented design, clean system structuring, and now database persistence using SQLite.

---

# 📌 Project Objective

Build a minimal banking engine that allows users to:

1. Create an account
2. Deposit money
3. Withdraw money
4. Check balance
5. Exit the system

The system now supports persistent storage using SQLite, ensuring data is retained even after the application closes.

---

# 🎯 Functional Requirements

## 1️⃣ Create Account
- User provides:
  - Name
  - Initial deposit amount
- System generates:
  - Unique account number
- Initial deposit must not be negative.
- Account data is stored in the SQLite database.

---

## 2️⃣ Deposit Money
- User provides:
  - Account number
  - Deposit amount
- System:
  - Verifies account exists
  - Verifies deposit amount is positive
  - Updates balance
  - Records transaction in database

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
  - Records transaction in database

---

## 4️⃣ Check Balance
- User provides:
  - Account number
- System:
  - Verifies account exists
  - Displays current balance (retrieved from database)

---

## 5️⃣ Exit
- Terminates application safely.
- Ensures database connection closes properly.

---

# 🏗 System Design

## 🔹 Architecture Type

Monolithic CLI application with object-oriented structure and SQLite persistence layer.

The system consists of:

- Account Entity
- BankingService (Business Logic Layer)
- AccountRepository (Database Layer)
- Main Application (Menu Loop)

---

# 🧠 Core Components

## 1️⃣ Account Class

### Responsibilities:
- Store account data
- Represent domain object
- Maintain balance integrity

### Attributes:
- accountNumber
- accountHolderName
- balance
- createdAt

Encapsulation principle:  
Balance should only be modified through controlled service logic.

---

## 2️⃣ BankingService Class

### Responsibilities:
- Validate user input
- Coordinate operations
- Apply business rules
- Call repository methods
- Ensure atomic transaction behavior

---

## 3️⃣ AccountRepository Class

### Responsibilities:
- Handle database connection
- Insert new accounts
- Update account balance
- Fetch account details
- Insert transaction records
- Retrieve transaction history

### Internal Storage:
SQLite database

Tables:

accounts  
- id (Primary Key)  
- account_number (Unique)  
- account_holder_name  
- balance  
- created_at  

transactions  
- id (Primary Key)  
- account_number (Foreign Key)  
- type (DEPOSIT / WITHDRAW)  
- amount  
- balance_after  
- timestamp  

Reason:
- Persistent storage
- Efficient lookup
- Audit trail support
- Professional backend design

---

## 4️⃣ Main Class

### Responsibilities:
- Display menu
- Accept user input
- Call BankingService methods
- Maintain program loop

---

# 🔁 Application Flow

1. Start Program
2. Establish Database Connection
3. Display Menu
4. Accept User Choice
5. Execute Selected Operation
6. Persist changes to database
7. Return to Menu
8. Repeat until Exit

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

Accounts are now stored using SQLite instead of in-memory Map.

Previous Design:
```bash
Map<Integer, Account>
```

Updated Design:
```bash
SQLite Database (accounts table + transactions table)
```

Why?
- Persistent storage
- Transaction logging
- Scalable architecture
- Future database migration ready

---

# 🧪 Edge Cases to Handle

- Invalid account number
- Negative deposit amount
- Withdrawal greater than balance
- Non-numeric input
- No accounts created yet
- Empty input
- Database connection failure

Handling edge cases increases system robustness.

---

# 📂 Updated Project Structure

```bash
banking-system-cli/
│
├── entities/
│   └── account.py
│
├── repository/
│   └── account_repository.py
│
├── services/
│   └── banking_service.py
│
├── database/
│   └── banking.db
│
├── main.py
├── README.md
└── notes.md
```

---

# 🚀 Development Roadmap

## Phase 1 – Basic Functionality ✅
- Implement Account class
- Implement BankingSystem logic
- Implement menu loop
- Add basic validation

## Phase 2 – SQLite Integration ✅
- Create SQLite database
- Design accounts and transactions tables
- Implement repository layer
- Replace in-memory storage with database

## Phase 3 – Improvements
- Add transaction history viewing
- Add timestamps
- Improve input validation
- Add formatted CLI output

## Phase 4 – Advanced Upgrade
- Add authentication (PIN system)
- Add account locking mechanism
- Implement atomic DB transactions
- Add unit testing

## Phase 5 – Full Backend Evolution
- Convert CLI to REST API (Flask / FastAPI)
- Add database migration to MySQL/PostgreSQL
- Add authentication & authorization
- Dockerize application
- Add CI/CD pipeline

---

# 📊 System Design Principles Applied

- Object-Oriented Programming
- Encapsulation
- Separation of Concerns
- Single Responsibility Principle
- Repository Pattern
- Layered Architecture
- Data Persistence
- Atomic Transactions

---

# 💡 Learning Goals

This project helps practice:

- OOP design
- Clean architecture thinking
- Input validation
- Error handling
- SQL schema design
- Database integration
- Backend logic structuring
- Migration-ready architecture

---

# ⚡ Philosophy

Build small systems.  
Design cleanly.  
Persist properly.  
Validate thoroughly.  
Improve iteratively.

---

# 📌 Notes

The system now supports persistent storage using SQLite.

Future improvements may include:
- Multi-user support
- REST API layer
- Frontend integration
- Production-level database migration

---

🏦 Built for backend logic mastery and database integration.