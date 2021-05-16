from tkinter import *
from tkinter import ttk
import tkinter 
from stockholm import Money

usd_rates = {"USD": 1, "EUR": 0.82, "GBP": 0.71, "JPY": 109.38, "NIO": 35.20}

eur_rates = {"USD": 1.21, "EUR": 1, "GBP": 0.86, "JPY": 132.87, "NIO": 42.75}

gbp_rates = {"USD": 1.41, "EUR": 1.16, "GBP": 1, "JPY": 154.18, "NIO": 49.61}

jpy_rates = {"USD": 0.0091, "EUR": 0.0075, "GBP": 0.0065, "JPY": 1, "NIO": 0.32}

nio_rates = {"USD": 0.029, "EUR": 0.024, "GBP": 0.020, "JPY": 3.13, "NIO": 1}

def select_rates(currency):
    rates = ""
    if currency == "USD":
        rates = usd_rates
        return rates
    elif currency == "EUR":
        rates = eur_rates
        return rates
    elif currency == "GBP":
        rates = gbp_rates
        return rates
    elif currency == "JPY":
        rates = jpy_rates
        return rates
    elif currency == "NIO":
        rates = nio_rates
        return rates

def convert_currency():
    conversion = ""
    value = input1.get()
    from_currency = from_box.get()
    to_currency = to_box.get()
    rate = select_rates(from_currency)

    while True:
        try:
            x = rate[to_currency]
            break
        except (TypeError, KeyError):
            print("No to currency selected")
            break

    if value != "" and from_currency != "" and to_currency != "":
        calculation = Money(value + " " + from_currency) * x
        conversion = Money(calculation).to_currency(to_currency)

    else:
        result_label["text"] = "Couldn't calculate :("
        print("No value or from/to currency selected")
    return conversion

def print_result():
    result = convert_currency()
    if result != "":
        print(result) #Debug tool
        result_label["text"] = result
    #else: 
        #print("NADA") #Debug tool

#I don't understand this class, I found it on StackOverflow. It is used to avoid any non int
#input inside entries.
class Lotfi(tkinter.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tkinter.StringVar()
        tkinter.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit(): 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)

window = Tk()
window.title("Currency Converter")
window.geometry("300x200")
window.resizable(False, False)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

main_label = Label(window, text="Currency Converter", pady=0, font=("helvetica", 15))
main_label.place(x=65, y=10)

#self.var is where the values of the input goes
input_label = Label(window, text="Amount", font=("helvetica", 9))
input_label.place(x=7, y=55)

input1_Var = StringVar()
input1 = Lotfi(window, bd=3, width=15)
input1.place(x=63, y=55)

from_label = Label(window, text="From", font=("helvetica", 9))
from_label.place(x=20, y=90)

currencyOption = ["USD", "EUR", "GBP", "JPY", "NIO"]
from_box = ttk.Combobox(window, values= currencyOption, width=5)
from_box.place(x=63, y=90)

to_label = Label(window, text="To", font=("helvetica", 9))
to_label.place(x=35, y=120)

to_box = ttk.Combobox(window, values= currencyOption, width=5)
to_box.place(x=63, y=120)

convert_btn = Button(window, text="Convert", width=10, bg="lightgrey", command=print_result)
convert_btn.place(x=62, y=155)

result_label = Label(window, text="", font=("helvetica", 10))
result_label.place(x=150, y=158)

window.mainloop()