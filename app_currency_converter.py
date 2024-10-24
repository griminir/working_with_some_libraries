def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('invalid amount')

def get_currency(label):
    currencies = ('NOK', 'USD', 'EUR')
    while True:
        currency = input(f'{label} currency (NOK/USD/EUR): ').upper()
        if currency not in currencies:
            print('invalid currency')
        else:
            return currency
        
def convert(amount, source_currency, target_currency):
    # as of 24.okt 2024
    exhange_rate = {
        'NOK': {'USD': 0.092, 'EUR': 0.085},
        'USD': {'NOK': 10.92, 'EUR': 0.93},
        'EUR': {'NOK': 11.79, 'USD': 1.08}
    }

    if source_currency == target_currency:
        return amount
    return amount * exhange_rate[source_currency][target_currency]

def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    print(f'{amount} {source_currency} = {converted_amount:.2f} {target_currency}')

# this stops it from being executed if the file is imported to reuse some of the functions
if __name__ == '__main__':
    main()