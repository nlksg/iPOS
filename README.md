# iPOS - Point of Sale System

A comprehensive Point of Sale (POS) system built with Django 5.2.5.

## Features

The iPOS system includes the following modules:
- **Users** - User management with role-based access (Admin, Manager, Cashier)
- **Products** - Product catalog with categories and variants
- **Sales** - Transaction processing and payment handling
- **Inventory** - Stock management and movement tracking
- **Purchases** - Supplier management and purchase orders
- **Customers** - Customer database with loyalty program support
- **Reports** - Business intelligence and reporting
- **Accounts** - Financial accounting with double-entry bookkeeping

## Quick Start

1. Install dependencies:
```bash
pip install Django==5.2.5
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser:
```bash
python manage.py createsuperuser
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Access the admin interface at http://127.0.0.1:8000/admin/

## App URLs

- Users: http://127.0.0.1:8000/users/
- Products: http://127.0.0.1:8000/products/
- Sales: http://127.0.0.1:8000/sales/
- Inventory: http://127.0.0.1:8000/inventory/
- Purchases: http://127.0.0.1:8000/purchases/
- Customers: http://127.0.0.1:8000/customers/
- Reports: http://127.0.0.1:8000/reports/
- Accounts: http://127.0.0.1:8000/accounts/

## Development

This project was bootstrapped using Django's built-in management commands and follows Django best practices for project structure and organization.