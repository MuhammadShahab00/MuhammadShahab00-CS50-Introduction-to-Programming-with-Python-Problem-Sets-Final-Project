import requests
from sys import argv, exit

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    exit()

res = response.json()
bitcoin_price = res['bpi']['USD']['rate'].replace(',', '')
bitcoin_price = float(bitcoin_price)

if len(argv) != 2:
    exit('Missing command-line argument')
else:
    try:
        quantity = float(argv[1])
    except:
        exit('Command-line argument is not a number')

total_price = quantity * bitcoin_price

print(f'${total_price:,.4f}')
