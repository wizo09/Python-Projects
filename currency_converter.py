import requests
import json


history = []
try:
    with open('converter.json', 'r') as f:
        history = json.load(f)

except FileNotFoundError:
    pass

api_key = '6e09f00c2e6e2224fff26eff'


def convert():
    from_currency = input('Convert from (e.g. USD): ').upper()
    to_currency = input('Convert to (e.g. NGN): ').upper()
    amount = float(input('Amount To Convert: '))

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()

    rate = data['conversion_rates'][to_currency]
    result = amount * rate
    history.append({'From currency': from_currency, 'To currency': to_currency, 'Amount': amount, 'Result': result})
    print(f'{amount} {from_currency} = {result:.2f} {to_currency}')

    print('===History===')
    for item in history:
        print(f"{item['Amount']} {item['From currency']}"
              f" = {item['Result']:.2f} {item['To currency']}")

while True:

    convert()
    play_again = input('Convert again? (yes/no): ')

    if play_again == 'no':
        with open('converter.json', 'w') as f:
            json.dump(history, f)
        print('Goodbye!')
        break