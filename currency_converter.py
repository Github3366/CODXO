import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception("Error fetching exchange rates. Please check your API key and internet connection.")
    
    rates = data['conversion_rates']
    if target_currency not in rates:
        raise Exception(f"Currency {target_currency} not found.")
    
    return rates[target_currency]

def currency_converter():
    api_key = "e2b788a92923fa50beb1ea0d"  # Replace with your actual API key
    print("Welcome to the Currency Converter!")

    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    try:
        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
        converted_amount = amount * exchange_rate
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency} at the current exchange rate.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    currency_converter()
