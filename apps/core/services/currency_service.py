import requests

class CurrencyService:
    BASE_URL = 'https://api.privatbank.ua/p24api/pubinfo'

    @classmethod
    def get_rates(cls):
        response = requests.get(
            cls.BASE_URL,
            params = {
                'json': '',
                'exchange': '',
                'coursid': 5
            }
        )

        response.raise_for_status()
        return response.json()
