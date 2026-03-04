from currency_converter import CurrencyConverter

c=CurrencyConverter()

amt=float(input(" enter your amount:-"))

new=c.convert(amt,'USD',"INR")

print(f'This usa dollers in indian rupees:-{new}')







