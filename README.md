# 📦 Inventory ERP System

A desktop-based **Inventory Management System** developed using **Python**, **CustomTkinter**, and **SQLite**. This application follows the **MVC (Model-View-Controller)** architecture with **Repository Pattern** and **Service Layer**, providing a clean, modular, and maintainable codebase.

---

## ✨ Features

### 📊 Dashboard
- Inventory summary
- Total products
- Total stock
- Inventory value
- Low stock monitoring
- Top selling products

### 📦 Product Management
- Add Product
- Edit Product
- Delete Product
- Search Product
- Category Management
- Stock Monitoring

### 🔄 Transaction Management
- Stock In
- Stock Out
- Search Transaction
- Filter Transaction
- Edit Transaction
- Delete Transaction
- Automatic Stock Validation

### 📑 Reports
- Dashboard Report
- Product Report
- Transaction Report
- Critical Stock Report
- Top Selling Report

### 📈 Excel Export
- Multi Sheet Report
- Financial Summary
- Styled Excel Report
- Charts

### 🔔 Notification Center
- Success Dialog
- Warning Dialog
- Error Dialog
- Confirmation Dialog

### ⚙ Settings
- Appearance Mode
- Confirm Delete
- Auto Refresh Dashboard
- Auto Open Excel
- Notification Settings

---

# 🏛 Architecture

```
GUI
 │
 ▼
Controller
 │
 ▼
Service
 │
 ▼
Repository
 │
 ▼
SQLite Database
```

Design Pattern

- MVC
- Repository Pattern
- Service Layer

---

# 🛠 Built With

- Python 3.11+
- CustomTkinter
- SQLite3
- OpenPyXL
- Matplotlib

---

# 📂 Project Structure

```
InventoryERP
│
├── config/
├── database/
├── repositories/
├── reports/
├── services/
├── ui/
│   ├── gui/
│   │   ├── components/
│   │   ├── controllers/
│   │   └── views/
├── utils/
│
├── main.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 🚀 Installation

Clone repository

```bash
git clone https://github.com/ariffadi/InventoryERP.git
```

Open project

```bash
cd InventoryERP
```

Create Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate Virtual Environment

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate
```

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
python main.py
```

---

# 📸 Screenshots

> Screenshots will be added soon.

- Dashboard
- Products
- Transactions
- Reports
- Settings

---

# 👨‍💻 Author

**Arif Fadi Maolana**

GitHub

https://github.com/ariffadi

---

# 📄 License

This project is licensed under the MIT License.
