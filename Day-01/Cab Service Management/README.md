# 🚖 Cab Services Management System

A simple console-based / backend-focused Cab Booking and Management System built to simulate real-world ride booking operations.

This project focuses on:
- Object-Oriented Design
- Clean Architecture
- Backend Logic Implementation
- Modular Code Structure

---

# 📌 Project Objective

To build a cab service platform that allows:

1. User Registration & Login  
2. Book a Cab  
3. Cancel a Ride  
4. View Ride History  
5. Driver Assignment  
6. Fare Calculation  
7. Admin Management  

The system runs without a GUI (for Phase 1) and can later be extended to a web/mobile application.

---

# 🏗️ System Design

## 👤 Users
- Register
- Login
- Book ride
- Cancel ride
- View ride history

## 🚗 Drivers
- Available / Busy status
- Assigned rides
- Earnings tracking

## 🛠️ Admin
- Add / Remove Drivers
- View all bookings
- Monitor revenue

---

# 🧱 Project Structure
```bash
CabService/
│
├── main.py
├── models/
│   ├── user.py
│   ├── driver.py
│   ├── ride.py
│
├── services/
│   ├── booking_service.py
│   ├── driver_service.py
│
├── utils/
│   ├── fare_calculator.py
│
└── README.md
```
---

# 🧠 Core Features

## 1️⃣ User Management
- Create account
- Login authentication
- Store ride history

## 2️⃣ Ride Booking
- Enter pickup location
- Enter drop location
- Auto driver assignment
- Fare calculation

## 3️⃣ Driver Management
- Driver availability tracking
- Assign nearest available driver
- Update status after ride completion

## 4️⃣ Fare Calculation

Fare Formula:
Fare = BaseFare + (Distance × CostPerKm)

---

# 🛠️ Technologies Used

- Python 3.x
- OOP (Object-Oriented Programming)
- CLI (Command Line Interface)
- Basic Data Structures (Lists, Dictionaries)

---

# 🔄 System Workflow

1. User logs in
2. User requests a ride
3. System checks available drivers
4. Assigns driver
5. Calculates fare
6. Ride completes
7. Driver marked available again

---

# 📊 Future Enhancements

- Database Integration (MySQL / PostgreSQL)
- Web Version (Django / Flask)
- Android App Version
- Online Payment Integration
- Real-time GPS Tracking
- Driver Rating System

---

# 🧪 Sample Use Case

1. Register User
2. Login
3. Book Ride
   - Pickup: City Center
   - Drop: Airport
4. Fare calculated: ₹450
5. Driver Assigned: Raj Patel
6. Ride Completed

---

# 📦 Installation & Setup

## 1️⃣ Clone the Repository

git clone https://github.com/yourusername/cab-services.git

## 2️⃣ Navigate to Project Directory

cd cab-services

## 3️⃣ Run the Application

python main.py

---

# 📐 Object-Oriented Design

## Classes Overview

### User
- user_id
- name
- phone
- ride_history

### Driver
- driver_id
- name
- vehicle_number
- is_available
- earnings

### Ride
- ride_id
- user
- driver
- pickup
- drop
- distance
- fare
- status

---

# 🏁 Project Status

Phase 1: CLI Version Completed  
Phase 2: Database Integration  
Phase 3: Web / Mobile Deployment  

---

# 🤝 Contribution

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request

---

# 📜 License

This project is open-source and available under the MIT License.