# 📘 Banking Core – Development Evolution Log

This document tracks the architectural and structural evolution of the Banking Core project.

The goal of this log is:
- To document learning progression
- To preserve architectural decisions
- To serve as a reference guide for future backend projects
- To build professional development habits

---

# 🚀 Phase 1 – Basic CLI Banking (Initial Objective)

### Goal:
Build a simple CLI banking system with:

- Create account
- Deposit
- Withdraw
- Check balance
- Exit

### Characteristics:
- No database
- In-memory storage
- Basic class-based design
- Direct logic handling inside CLI

### Learning:
- Basic OOP
- Class structure
- Method interaction
- Simple validation

---

# 💾 Phase 2 – SQLite Integration

### Upgrade:
Replace in-memory storage with SQLite persistence.

### Changes:
- Introduced `sqlite3`
- Created `accounts` and `transactions` tables
- Implemented commit / rollback handling
- Ensured atomic transactions

### Architectural Impact:
- Data persists after application closes
- Introduced real database constraints
- Learned transaction safety

---

# 🏗 Phase 3 – Repository Pattern

### Problem:
Business logic and SQL were mixed.

### Solution:
Created `AccountRepository` layer.

### Responsibilities:
- Handle SQL queries
- Manage DB connection
- Map DB rows
- Commit / rollback

### Result:
- Separation of concerns
- Service layer isolated from SQL
- Cleaner architecture

---

# 🧠 Phase 4 – Service Layer (Business Logic Isolation)

### Introduced:
`BankingServices` layer

### Responsibilities:
- Input validation
- Business rules
- Transaction control
- Raising domain errors

### Benefits:
- No SQL in business logic
- Atomic operation control
- Clear responsibility separation

---

# 📦 Phase 5 – Domain Entities

### Added:
- `Account` entity
- `Transaction` entity

### Before:
Repository returned tuples.

### After:
Repository maps DB rows → Entity objects.

### Improvement:
- Removed tuple indexing (e.g., account[2])
- Improved readability (account.balance)
- Decoupled service layer from DB structure

---

# ⚠️ Phase 6 – Custom Exception Architecture

### Introduced:
Custom domain exception hierarchy:

- BankingException (Base)
- AccountNotFoundException
- InvalidAmountException
- InsufficientBalanceException
- InvalidAccountNameException

### Benefits:
- Clear domain error semantics
- Business errors separated from system errors
- REST API ready error mapping

---

# 🖥 Phase 7 – Thin CLI Controller

### Final CLI Structure:
- main.py acts as controller
- Only interacts with service layer
- No SQL in CLI
- Catches BankingException separately

### Architectural Model:

```bash
CLI → Service → Repository → SQLite  
            ↑  
         Entities  
```

---

# 🧩 Final Architecture Summary

The system now follows:

- Clean layered architecture
- Repository pattern
- Domain modeling
- Atomic transactions
- Dependency injection
- Custom exception hierarchy
- Persistence with SQLite

---

# 🧠 Key Engineering Lessons Learned

1. Separate business logic from database logic.
2. Never expose raw DB rows to service layer.
3. Use entities for domain modeling.
4. Use custom exceptions for semantic clarity.
5. Keep CLI thin.
6. Control transactions in service layer.
7. Design for future scalability (REST-ready).

---

# 🎯 Current System State

The project is now:

- Resume-level backend core
- REST API ready
- Structurally scalable
- Cleanly layered

---

# 🚀 Next Possible Evolution Paths

- Add Flask REST API
- Add Authentication (PIN system)
- Add Logging layer
- Add Dockerization
- Convert to MySQL/PostgreSQL
- Add unit testing

---

# 📌 Personal Reflection

The project began as a small CLI tool.

It evolved into a structured backend system with:

- Clear architecture
- Domain separation
- Production-style patterns

This log marks the completion of the CLI backend foundation phase.