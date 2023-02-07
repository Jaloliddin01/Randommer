import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        headers = {'X-Api-Key': api_key}
        url = f'{self.base_url}Finance/CryptoAddress/Types'
        response = requests.get(url, headers=headers)
        return response.json()

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        headers = {'X-Api-Key': api_key}
        payload = {'cryptoType': crypto_type}
        url = f'{self.base_url}Finance/CryptoAddress'
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        headers = {'X-Api-Key': api_key}
        url = f'{self.base_url}Finance/Countries'
        response = requests.get(url, headers=headers)
        return response.json()

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        headers = {'X-Api-Key': api_key}
        url = f'{self.base_url}Finance/Iban/{country_code}'
        response = requests.get(url, headers=headers)
        return response.json()

apikey = '1342a09ae7384e94a5aa8f52febf9fa3'
obj = Finance()
print(obj.get_crypto_address_types(apikey))
print(obj.get_crypto_address(crypto_type = '12', api_key = apikey))
print(obj.get_countries(apikey))
print(obj.get_iban_by_country_code('DE', apikey))
