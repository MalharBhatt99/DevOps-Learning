# 🏦 Banking Core System

A layered, console-based banking system built using Python and SQLite.  
This project simulates core banking operations while demonstrating clean architecture principles, database persistence, and structured backend design.

---

## 📌 Overview

The Banking System CLI is a backend-focused application that allows users to:

- Create accounts  
- Deposit funds  
- Withdraw funds  
- View account balance  
- View transaction history  

Unlike a basic CLI tool, this system implements:

- Layered Architecture  
- Repository Pattern  
- Domain Entities  
- Custom Exception Hierarchy  
- SQLite Persistence  
- Atomic Transaction Handling  

All data is stored in a SQLite database, ensuring persistence across application restarts.

---

## 🏗 Architecture

The application follows a layered backend structure:

```bash
CLI (main.py)
↓
Service Layer (Business Logic)
↓
Repository Layer (Data Access)
↓
SQLite Database
```

---


### 🔹 Layers

#### 1️⃣ Entities (Domain Models)
- `Account`
- `Transaction`

These represent core business objects and abstract database structure from the service layer.

#### 2️⃣ Service Layer (`BankingServices`)
Responsible for:
- Input validation  
- Business rule enforcement  
- Coordinating operations  
- Managing atomic database transactions  
- Raising domain-specific exceptions  

#### 3️⃣ Repository Layer (`AccountRepository`)
Responsible for:
- Database connection handling  
- SQL execution  
- CRUD operations  
- Mapping database rows to entity objects  

#### 4️⃣ CLI Controller (`main.py`)
Responsible for:
- User interaction  
- Menu rendering  
- Calling service methods  
- Handling exceptions  

---

## 💾 Database Design

SQLite is used for persistent storage.

### `accounts` Table
```bash
| Column              | Description                     |
|---------------------|---------------------------------|
| id                  | Primary key                     |
| account_number      | Unique account identifier       |
| account_holder_name | Account owner name              |
| balance             | Current account balance         |
| created_at          | Account creation timestamp      |
```
---

### `transactions` Table
```bash
| Column         | Description                              |
|----------------|------------------------------------------|
| id             | Primary key                              |
| account_number | Foreign key reference to accounts table  |
| type           | DEPOSIT / WITHDRAW / INITIAL DEPOSIT     |
| amount         | Transaction amount                       |
| balance_after  | Balance after transaction                |
| timestamp      | Transaction timestamp                    |
```
This structure provides:

- Persistent storage  
- Audit trail  
- Transaction history  
- Future migration flexibility  

---

## 🎯 Core Features

### ✅ Account Creation
- Validates account holder name  
- Validates initial deposit  
- Auto-generates unique account number  
- Records initial deposit transaction  

### ✅ Deposit
- Validates account existence  
- Validates positive amount  
- Updates balance  
- Logs transaction  

### ✅ Withdrawal
- Validates account existence  
- Validates positive amount  
- Checks sufficient balance  
- Updates balance  
- Logs transaction  

### ✅ View Balance
- Retrieves current balance from database  

### ✅ View Transaction History
- Displays full transaction log  
- Shows transaction type, amount, balance after, and timestamp  

---

## ⚠️ Exception Architecture

The system uses a custom exception hierarchy:

- `BankingException` (Base class)  
- `AccountNotFoundException`  
- `InvalidAmountException`  
- `InsufficientBalanceException`  
- `InvalidAccountNameException`  

This ensures:

- Clean separation of business errors  
- Controlled error handling  
- REST API readiness  

---

## 🧪 Validation Rules

- Account name must not be empty  
- Initial deposit must be ≥ 0  
- Deposit amount must be > 0  
- Withdrawal amount must be > 0  
- Withdrawal must not exceed balance  
- Account must exist before any operation  

---

## 📂 Project Structure

```bash
banking-core/
│
├── entities/
│ ├── account.py
│ └── transaction.py
│
├── repository/
│ └── account_repository.py
│
├── services/
│ └── banking_services.py
│
├── exceptions/
│ ├── base_exception.py
│ ├── account_not_found_exception.py
│ ├── invalid_amount_exception.py
│ ├── insufficient_balance_exception.py
│ └── invalid_account_name_exception.py
│
├── database/
│ └── accounts.db
│
├── docs/
│ └── development_log.md
│
├── main.py
└── README.md
```

---

## 🚀 Development Phases

### Phase 1 – CLI Foundation
- Basic account operations  
- In-memory storage  
- Core OOP structure  

### Phase 2 – SQLite Integration
- Database schema design  
- Repository implementation  
- Persistent storage  
- Transaction logging  

### Phase 3 – Architecture Refinement
- Entity modeling  
- Layer separation  
- Custom exception hierarchy  
- Atomic transaction control  

### Phase 4 – Future Enhancements (Planned)
- PIN-based authentication  
- Account locking mechanism  
- Logging layer  
- Unit testing  
- REST API migration (Flask / FastAPI)  
- MySQL/PostgreSQL migration  
- Dockerization  

---

## 🧠 Engineering Principles Applied

- Object-Oriented Programming  
- Separation of Concerns  
- Single Responsibility Principle  
- Repository Pattern  
- Layered Architecture  
- Dependency Injection  
- Atomic Transactions  
- Domain Modeling  

---

## 📘 Development Journey

For a detailed architectural evolution and learning progression, see:
```bash
docs/development_log.md
```

---

## 🎓 Learning Outcomes

This project demonstrates:

- Backend architecture design  
- Database integration  
- Transaction management  
- Clean error modeling  
- Domain-driven structuring  
- Scalable system thinking  

---

## ⚡ Philosophy

Start simple.  
Refactor intentionally.  
Separate responsibilities.  
Persist safely.  
Design for evolution.  

---

🏦 Built as a backend architecture learning project with real database integration.