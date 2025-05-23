# 🧾 Personal Budget Manager

A command-line based personal budget management system built using Python, MySQL, and Matplotlib. This tool allows users to manage their income, expenses, and investments, and visualize financial statistics including savings and return calculations.

---

## 📦 Features

- **User Authentication** (with hashed passwords)
- **Income Management**
  - Add one-time, monthly, or yearly income
  - View or delete income entries
- **Expense Tracking**
  - Fixed expenses (subscriptions)
  - Variable expenses
- **Investment Portfolio**
  - Add and manage investments
  - Calculate projected returns
- **Statistics Dashboard**
  - Visual pie charts for income, expenses, investments, and savings
- **Persistent Data Storage** using MySQL

---

## 🛠️ Technologies Used

- **Python 3**
- **MySQL** (via `mysql-connector-python`)
- **Matplotlib** (for visualizations)
- **Hashlib** (for password security)

---

## ⚙️ Setup Instructions

1. **Install Python Dependencies**

```bash
pip install mysql-connector-python matplotlib
```

2. **Set Up MySQL Database**

Log into your MySQL server and run the following to set up the schema:

```sql
CREATE DATABASE Budget_Manager;

USE Budget_Manager;

CREATE TABLE User_Details (
    Username VARCHAR(255),
    Password VARCHAR(255),
    KeyID VARCHAR(64)
);

CREATE TABLE Income (
    Source VARCHAR(255),
    Value INT,
    KeyID VARCHAR(64)
);

CREATE TABLE Subscriptions (
    Name VARCHAR(255),
    Price INT,
    KeyID VARCHAR(64)
);

CREATE TABLE Variable_Expense (
    Name VARCHAR(255),
    Price INT,
    KeyID VARCHAR(64)
);

CREATE TABLE Investments (
    Investment VARCHAR(255),
    Invested_amount INT,
    KeyID VARCHAR(64)
);
```

3. **Update Database Credentials**

Edit the Python script to reflect your MySQL credentials:

```python
Con_obj = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    autocommit=True
)
```

---

## 🚀 How to Run

```bash
python "Budget python.py"
```

Follow the interactive prompts in the terminal to log in, manage your finances, and view statistics.

---

## 📊 Sample Visual Output

The application displays pie charts to represent:
- Income Distribution
- Expense Breakdown
- Investment Portfolio
- Overall Savings Distribution

All charts are generated dynamically based on your entries.

---

## 🛡️ Security

- Passwords are stored using **SHA-256 hashing** (never stored in plain text).
- Each user is uniquely identified by a hash-based `KeyID`.

---

## 📌 Notes

- All user data is stored in MySQL, organized by user `KeyID`.
- Application is intended for **single-user CLI usage** and not production web deployment.
