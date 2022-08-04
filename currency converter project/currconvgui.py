import tkinter as tk
import customtkinter as ctk
import requests


def fetch_currencies_data(source: str):
    if is_normal(source):
        source = "symbols"
    else:
        source = "cryptocurrencies"
    url = f"https://api.exchangerate.host/{source}"
    data = requests.get(url).json()[source]
    return data


def fetch_convert(source: str, currency1: str, currency2: str, amount: float):
    url = f"https://api.exchangerate.host/convert?source={source}&from={currency1}&to={currency2}&amount={amount}"
    data = requests.get(url).json()
    return data_to_string(source, data)


def data_to_string(source: str, data: dict):
    currency1 = data["query"]["from"]
    currency2 = data["query"]["to"]
    amount = data["query"]["amount"]
    rate = data["info"]["rate"]
    result = data["result"]
    currencies_data = data_of(source)
    if is_normal(source):
        currency1_desc = currencies_data[currency1]["description"]
        currency2_desc = currencies_data[currency2]["description"]
    else:
        currency1_desc = currencies_data[currency1.lower()]["name"]
        currency2_desc = currencies_data[currency2.lower()]["name"]
    string = f"{amount} {currency1} ({currency1_desc}) is {result} {currency2} ({currency2_desc})\nrate: {rate}"
    return string


def currencies_data_to_list(source: str, currencies_data: dict):
    if is_normal(source):
        currencies_list = list(currencies_data.keys())
    else:
        currencies_list = []
        for i in currencies_data:
            currencies_list.append(currencies_data[i]["symbol"])
    currencies_list.sort()
    return currencies_list


def calculate_button(source: str, currency1: str, currency2: str, amount: str):
    string = formatter(source, currency1, currency2, amount)
    write_text_box(string)


def formatter(source: str, currency1: str, currency2: str, amount: str):
    error = error_check(source, currency1, currency2, amount)
    if error == "None":
        amount = float(amount)
        return fetch_convert(source, currency1, currency2, amount)
    else:
        return error


def error_check(source: str, currency1: str, currency2: str, amount: str):
    if amount.lstrip("-").isdigit():
        amount = float(amount)
    else:
        return "Please enter a number"
    if currency1 not in currency_list(source) or currency2 not in currency_list(source):
        return "Please enter the correct currency"
    if amount < 0:
        return "Please enter a positive number"
    return "None"


def currency_list(source: str):
    return currencies_data_to_list(source, data_of(source))


def data_of(source: str):
    if is_normal(source):
        return normal_data
    else:
        return crypto_data


def is_normal(source: str):
    if source == "":
        return True
    else:
        return False


def write_text_box(string: str):
    textbox.configure(state=ctk.NORMAL)
    textbox.delete(1.0, ctk.END)
    textbox.insert(ctk.END, string)
    textbox.configure(state=ctk.DISABLED)


root = ctk.CTk()
root.title("Currency converter")

source = ctk.StringVar()

normal_data = fetch_currencies_data("")
crypto_data = fetch_currencies_data("crypto")


topframe = ctk.CTkFrame(root)
topframe.pack(ipady=10, ipadx=10, pady=10, padx=10)
bottomframe = ctk.CTkFrame(root)
bottomframe.pack(ipady=10, ipadx=10, pady=10, padx=10)

ctk.CTkLabel(topframe, text="first currency").grid(row=0, column=0)
ctk.CTkLabel(topframe, text="second currency").grid(row=0, column=1)
ctk.CTkLabel(topframe, text="amount").grid(row=0, column=2)

textentry1 = ctk.CTkEntry(topframe, width=100)
textentry1.grid(row=1, column=0, padx=20, pady=5)
textentry2 = ctk.CTkEntry(topframe, width=100)
textentry2.grid(row=1, column=1, padx=20, pady=5)
textentry3 = ctk.CTkEntry(topframe, width=100)
textentry3.grid(row=1, column=2, padx=20, pady=5)

textbox = tk.Text(bottomframe, wrap=ctk.WORD, cursor="arrow", state=ctk.DISABLED, bg="#2a2d2e", bd=0, fg="white", selectbackground="#2a2d2e")
textbox.pack(padx=10, pady=10)

ctk.CTkButton(topframe, text="Calculate", command=lambda: calculate_button(source.get(), textentry1.get().upper(), textentry2.get().upper(), textentry3.get()), width=100).grid(row=1, column=3, padx=20, pady=5)
ctk.CTkButton(topframe, text="List currencies", command=lambda: write_text_box(currency_list(source.get())), width=100).grid(row=3, column=3, padx=20, pady=5)

ctk.CTkRadioButton(topframe, text="normal", variable=source, value="").grid(row=2, column=0)
ctk.CTkRadioButton(topframe, text="crypto", variable=source, value="crypto").grid(row=3, column=0)

root.mainloop()
