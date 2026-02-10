import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_cpf(cpf):
    # Add CPF validation logic here.
    pass  # Placeholder


def validate_cnpj(cnpj):
    # Add CNPJ validation logic here.
    pass  # Placeholder


def validate_phone(phone):
    pattern = r'^(\+\d{1,3}( )?)?\d{10}$'  # Example pattern
    return re.match(pattern, phone) is not None


def validate_username(username):
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return re.match(pattern, username) is not None


def validate_password(password):
    # Example: At least one uppercase, one lowercase, one digit, and min 8 chars
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password) is not None
