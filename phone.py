import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        headers = {'X-Api-Key': api_key}
        payload = {'CountryCode': CountryCode, 'Quantity': Quantity}
        url = f'{self.base_url}Phone/Generate'
        response = requests.get(url, headers=headers, params=payload)
        return response.json()
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        headers = {'X-Api-Key': api_key}
        payload = {'Quantity': Quantity}
        url = f'{self.base_url}Phone/IMEI'
        response = requests.get(url, headers=headers, params=payload)
        return response.json()
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        headers = {'X-Api-Key': api_key}
        payload = {'telephone': telephone, 'CountryCode': CountryCode}
        url = f'{self.base_url}Phone/Validate'
        response = requests.get(url, headers=headers, params=payload)
        return response.json()
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        headers = {'X-Api-Key': api_key}
        url = f'{self.base_url}Phone/Countries'
        response = requests.get(url, headers=headers)

        return response.json()

apikey = '1342a09ae7384e94a5aa8f52febf9fa3'
obj = Phone()
print(obj.generate(apikey, 'uz', 5))
print(obj.get_IMEI(apikey, 5))
print(obj.is_valid(apikey, '+998909999999', 'uz'))
print(obj.get_countries(apikey))
