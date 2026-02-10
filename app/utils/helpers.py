from datetime import datetime, timedelta
import json
import csv

# Utility functions to handle common tasks

def format_date(date):
    return date.strftime('%Y-%m-%d')


def format_currency(amount, currency='$'):
    return f'{currency}{amount:,.2f}'


def format_phone_number(phone):
    # Example formatting for a Brazilian phone number
    return f'({phone[:2]}) {phone[2:7]}-{phone[7:]}'


def format_cpf(cpf):
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def format_cnpj(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'


def export_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


def export_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def calculate_color(priority):
    colors = {"high": "#FF0000", "medium": "#FFFF00", "low": "#00FF00"}
    return colors.get(priority, '#FFFFFF')


def get_text_initials(text):
    return ''.join([word[0].upper() for word in text.split() if word])


def truncate_text(text, length):
    return text[:length] + '...' if len(text) > length else text


def get_month_names():
    return [datetime(2020, i, 1).strftime('%B') for i in range(1, 13)]


def calculate_days_until(target_date):
    return (target_date - datetime.utcnow()).days
