import os

SECRET_KEY = os.getenv('SECRET_KEY')

# Replace with your actual sensitive data
PII_DATA = [
    {'name': 'John Doe', 'email': 'johndoe@example.com', 'address': '123 Main St, Anytown, CA', 'phone': '555-123-4567'},
    {'name': 'Jane Smith', 'email': 'janesmith@example.com', 'address': '456 Elm St, Anytown, CA', 'phone': '555-987-6543'}
]

FINANCIAL_DATA = [
    {'credit_card': '1234567890123456', 'account_number': '1234567890'},
    {'credit_card': '9876543210987654', 'account_number': '9876543210'}
]
