<<<<<<< HEAD
import requests
import sys
import os

def main():

    #api_key = os.environ.get("BITCOIN_KEY")
    api_key = "81cbcfffe2a69cf2ee8a8ad3f840d884434b523189a1acfa7118148d83f3f4e4"
    try:

        if not api_key:
            sys.exit("API key not found")

        # INPUT CHECKER
        if len(sys.argv) != 2:
            sys.exit("Please, only input the value in USD. e.g.: python bitcoin.py 10")

        # VALUE OF INPUT CHECKER
        amount_usd = float(sys.argv[1])
        if amount_usd < 0:
            sys.exit("Please, use a positive numbers")


        result = bitcoin_price(api_key) * float(sys.argv[1])
        print(f"${result:,.4f}")

    except ValueError:
        sys.exit("Please, use only positive-float numbers")

def bitcoin_price(api_key):
    """
    Fetch the current Bitcoin price in USD from the CoinCap API.

    The API key is read from an environment variable.

    Returns:
        float: Current Bitcoin price in USD.

    Raises:
        RuntimeError: If the API key is missing or invalid.
        requests.RequestException: If the HTTP request fails
    """
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
    true_site = requests.get(url)
    site_json = true_site.json()
    data = site_json["data"]
    price_for_usd = data["priceUsd"]
    return float(price_for_usd)

if __name__ == "__main__":
=======
import requests
import sys
import os

def main():

    #api_key = os.environ.get("BITCOIN_KEY")
    api_key = "81cbcfffe2a69cf2ee8a8ad3f840d884434b523189a1acfa7118148d83f3f4e4"
    try:

        if not api_key:
            sys.exit("API key not found")

        # INPUT CHECKER
        if len(sys.argv) != 2:
            sys.exit("Please, only input the value in USD. e.g.: python bitcoin.py 10")

        # VALUE OF INPUT CHECKER
        amount_usd = float(sys.argv[1])
        if amount_usd < 0:
            sys.exit("Please, use a positive numbers")


        result = bitcoin_price(api_key) * float(sys.argv[1])
        print(f"${result:,.4f}")

    except ValueError:
        sys.exit("Please, use only positive-float numbers")

def bitcoin_price(api_key):
    """
    Fetch the current Bitcoin price in USD from the CoinCap API.

    The API key is read from an environment variable.

    Returns:
        float: Current Bitcoin price in USD.

    Raises:
        RuntimeError: If the API key is missing or invalid.
        requests.RequestException: If the HTTP request fails
    """
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
    true_site = requests.get(url)
    site_json = true_site.json()
    data = site_json["data"]
    price_for_usd = data["priceUsd"]
    return float(price_for_usd)

if __name__ == "__main__":
>>>>>>> 7da541f6bd82c4034928e78fa215699c606660b5
    main()