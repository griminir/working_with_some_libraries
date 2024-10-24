while True:
    try:
        amount = float(input('Enter the amount: '))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print('invalid amount')

currencies = ('NOK', 'USD', 'EUR')

while True:
    source_currency = input('convert from (NOK/USD/EUR): ').upper()
    if source_currency not in currencies:
        print('invalid currency')
    else:
        break

while True:
    target_currency = input('convert to (NOK/USD/EUR): ').upper()
    if target_currency not in currencies:
        print('invalid currency')
    else:
        break

# as of 24.okt 2024
exhange_rate = {
    'NOK': {'USD': 0.092, 'EUR': 0.085},
    'USD': {'NOK': 10.92, 'EUR': 0.93},
    'EUR': {'NOK': 11.79, 'USD': 1.08}
}

if source_currency == target_currency:
    converted_amount = amount
else:
    converted_amount = amount * exhange_rate[source_currency][target_currency]
print(f'{amount} {source_currency} = {converted_amount:.2f} {target_currency}')