import requests


def get_exchange_rate(base_currency, target_currency):
    url = f'https://api.exchangerate.host/latest?base={base_currency}'
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]


output = get_exchange_rate("USD", 'KRW')
from pprint import pprint
pprint(output)