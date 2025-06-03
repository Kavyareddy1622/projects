def amount():
    while True:
        try:
            amount = float(input('enter amount:'))
            if amount <= 0:
                print('invalid input')
            else:
                return amount
        except ValueError:
            print('invalid input')

def currency(prompt):
    while True:
        currencies = ('INR', 'AED', 'USD')
        currency = input(f'enter {prompt} currency (INR/AED/USD):').upper()
        if currency not in currencies:
            print('invalid input')
        else:
            return currency

def convert(amount, source_currency, target):
    exchange_rate = {
        'INR': {'AED': 0.043, 'USD': 0.012},
        'AED': {'INR': 22.5, 'USD': 0.27},
        'USD': {'AED': 3.67, 'INR': 85.54}
    }
    if source_currency == target:
        return amount
    else:
        return amount * exchange_rate[source_currency][target]

def main():
    amount_value = amount()
    source_currency = currency('source')
    target_currency = currency('target')
    converted = convert(amount_value, source_currency, target_currency)
    print(f'{amount_value} {source_currency} is equal to {converted} {target_currency}')

if __name__ == "__main__":
    main()