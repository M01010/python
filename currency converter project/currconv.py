import requests


def fetch_currencies_data(source: str):
    if source == "":
        source = "symbols"
    elif source == "crypto":
        source = "cryptocurrencies"
    url = f"https://api.exchangerate.host/{source}"
    data = requests.get(url).json()
    return data[source]


def fetch_data_to_string(source: str, currency1: str, currency2: str, amount: float):
    url = f"https://api.exchangerate.host/convert?source={source}&from={currency1}&to={currency2}&amount={amount}"
    data = requests.get(url).json()
    rate = data["info"]["rate"]
    result = data["result"]
    if source == "":
        currencies_data = fetch_currencies_data("symbols")
        currency1_desc = currencies_data[currency1]["description"]
        currency2_desc = currencies_data[currency2]["description"]
    elif source == "crypto":
        currencies_data = fetch_currencies_data("cryptocurrencies")
        currency1_desc = currencies_data[currency1.lower()]["name"]
        currency2_desc = currencies_data[currency2.lower()]["name"]
    stringoutput = f"{amount} {currency1} ({currency1_desc}) is {result} {currency2} ({currency2_desc})\nrate: {rate}"
    return stringoutput


def set_currency(number: str, currencies_list: list):
    while True:
        x = input(f"enter {number} currency ").upper()
        if x in currencies_list:
            return x
        else:
            print(f"Currencies: {currencies_list}")


def set_amount(currency: str):
    while True:
        try:
            x = float(input(f"Please enter amount in {currency} "))
            return x
        except ValueError:
            continue


def currencies_data_to_list(source: str, currencies_data: dict):
    if source == "":
        currencies_list = list(currencies_data.keys())
        return currencies_list
    elif source == "crypto":
        currencies_list = []
        for i in currencies_data:
            currencies_list.append(currencies_data[i]["symbol"])
        return currencies_list


def set_source():
    while True:
        entry = input("crypto/normal? ").lower()
        if entry == "normal":
            return ""
        elif entry == "crypto":
            return "crypto"


source = set_source()
first_currency = set_currency("first", currencies_data_to_list(source, fetch_currencies_data(source)))
second_currency = set_currency("second", currencies_data_to_list(source, fetch_currencies_data(source)))
amount = set_amount(first_currency)
print(fetch_data_to_string(source, first_currency, second_currency, amount))
