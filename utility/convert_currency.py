import requests


def convert_currency_to_gbp(from_currency, initial_amount, final_amount):

    currency_list = call_currency_rate_api().json()

    if from_currency.lower() in currency_list["gbp"]:
        exchange_rate = currency_list["gbp"][from_currency.lower()]

        converted_initial_amount = round(initial_amount * exchange_rate, 2)
        converted_final_amount = round(final_amount * exchange_rate, 2)

    return {
        "exchange_rate_date": currency_list["date"],
        "converted_initial_amount": converted_initial_amount,
        "converted_final_amount": converted_final_amount,
    }


def call_currency_rate_api():
    try:
        respones = requests.get(
            "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/gbp.json"
        )
        return respones
    except Exception as e:
        return "Failed to call the api, try again later"
