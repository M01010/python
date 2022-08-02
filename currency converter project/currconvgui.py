import tkinter as tk
import customtkinter as ctk
import requests

root = ctk.CTk()


def fetch_currencies_data(source: str):
    if source == "":
        source = "symbols"
    elif source == "crypto":
        source = "cryptocurrencies"
    url = f"https://api.exchangerate.host/{source}"
    data = requests.get(url).json()
    return data[source]


def fetch_data_to_string(source: str, currency1: str, currency2: str, amount: float):
    if source == "" and (currency1 not in normal_list or currency2 not in normal_list):
            return "Wrong currency"
    elif source == "crypto" and (currency1 not in crypto_list or currency2 not in crypto_list):
            return "Wrong currency"
    elif amount < 0:
        return "please enter a correct amount"
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


def currencies_data_to_list(source: str, currencies_data: dict):
    if source == "":
        currencies_list = list(currencies_data.keys())
    elif source == "crypto":
        currencies_list = []
        for i in currencies_data:
            if not ("REALT" in currencies_data[i]["symbol"]):
                currencies_list.append(currencies_data[i]["symbol"])
    currencies_list.sort()
    return currencies_list


def calculate():
    if textentry3.get().isdigit():
        amount = float(textentry3.get())
    else:
        amount = -1
    string = fetch_data_to_string(source.get(), textentry1.get().upper(), textentry2.get().upper(), amount)
    textbox.configure(state=tk.NORMAL)
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, string)
    textbox.configure(state=tk.DISABLED)


def refresh_list(source):
    if source == "":
        list = currencies_data_to_list("", normal_list)
    elif source == "crypto":
        list = currencies_data_to_list("crypto", crypto_list)
    currency_list_box.delete(0, tk.END)
    for i in (list):
        currency_list_box.insert(tk.END, i)


source = tk.StringVar()
normal_list = fetch_currencies_data("")
crypto_list = fetch_currencies_data("crypto")

topframe = ctk.CTkFrame(root)
topframe.pack(pady=10, padx=10)
bottomframe = ctk.CTkFrame(root)
bottomframe.pack(pady=10, padx=10)

text1 = ctk.CTkLabel(topframe, text="first currency")
text1.grid(row=0, column=0)
text2 = ctk.CTkLabel(topframe, text="second currency")
text2.grid(row=0, column=1)
text3 = ctk.CTkLabel(topframe, text="amount")
text3.grid(row=0, column=2)

textentry1 = ctk.CTkEntry(topframe, width=50)
textentry1.grid(row=1, column=0, padx=5, pady=5)
textentry2 = ctk.CTkEntry(topframe, width=50)
textentry2.grid(row=1, column=1, padx=5, pady=5)
textentry3 = ctk.CTkEntry(topframe, width=50)
textentry3.grid(row=1, column=2, padx=5, pady=5)

button_calc = ctk.CTkButton(topframe, text="Calculate", command=calculate, width=50)
button_calc.grid(row=1, column=3, padx=5, pady=5)

rad1 = ctk.CTkRadioButton(topframe, text="normal", variable=source, value="", command=lambda : refresh_list(""))
rad1.grid(row=2, column=0, padx=5, pady=5)
rad2 = ctk.CTkRadioButton(topframe, text="crypto", variable=source, value="crypto", command=lambda : refresh_list("crypto"))
rad2.grid(row=2, column=1, padx=5, pady=5)

currency_list_box = tk.Listbox(bottomframe, bg="#292929", fg="white", height=10)
refresh_list(source.get())
currency_list_box.grid(row=0, column=0)

textbox = tk.Text(bottomframe, wrap=tk.WORD, state=tk.DISABLED, bg="#292929", height=10, width=50, bd=0, fg="white")
textbox.grid(row=0, column=1, columnspan=3)

root.mainloop()
