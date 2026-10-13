# Python ATM Simulator

A command-line Automated Teller Machine (ATM) application written in Python. This project simulates core banking operations with user authentication, transactional validation, and account state management.

---

## 🚀 Features & Capabilities

- **User Authentication:** 
  - PIN verification with a maximum of 3 login attempts before access is locked.
- **Account Management & Transactions:**
  - **Check Balance (`c`):** Instant display of current account balance in NIS.
  - **Quick & Custom Withdrawals (`w`):** Preset withdrawal options (50, 100, 200, 500 NIS) or user-specified custom amounts with balance validation.
  - **Deposits (`d`):** Minimum deposit validation (20 NIS minimum) to ensure valid transactions.
  - **PIN Change (`p`):** Option to update current PIN code.
  - **Transaction Receipt (`r`):** Generates a detailed receipt formatted with timestamps using Python's `datetime` module.
- **Interactive Session Loop:**
  - Multi-user session switching with options to log in as another user or shut down the ATM system safely.

---

## 🛠️ Key Python Concepts Demonstrated

1. **Data Structures:** Utilization of nested dictionaries (`dict`) for managing customer account states (`name`, `pin`, `balance`).
2. **Control Flow & Error Handling:** `while` loops for interactive menus, `if/elif/else` branching, and `try/except` blocks for handling invalid inputs (e.g., non-numeric entries).
3. **Modular Code Structure:** Functions with clear responsibilities (`login()`, `handle_withdrawal()`, `handle_deposit()`, `change_pin()`, `print_recipe()`, `atm_menu()`).
4. **Built-in Modules:** Use of `datetime` for real-time transaction timestamping.

---

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/AlonPerry/pythonATM.git](https://github.com/AlonPerry/pythonATM.git)
   cd pythonATM
