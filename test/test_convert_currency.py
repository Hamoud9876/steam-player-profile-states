from src.convert_currency import convert_currency_to_gbp, call_currency_rate_api


class TestCurrencyAPI:
    def test_currency_api_status_code_200(self):
        result = call_currency_rate_api()
        assert result.status_code == 200

    def test_currency_api_returns_list_of_currency_rate_with_gbp_base(self):
        result = call_currency_rate_api()

        assert "gbp" in result.json()
        assert "usd" in result.json()["gbp"]


class TestConvertCurrency:
    def test_conver_currency_return_dict(self):
        result = convert_currency_to_gbp("usd", 1, 1)

        assert isinstance(result, dict)
        assert isinstance(result["exchange_rate_date"], str)
        assert isinstance(result["converted_initial_amount"], float)
        assert isinstance(result["converted_final_amount"], float)



