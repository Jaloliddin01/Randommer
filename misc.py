import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        headers = {'X-Api-Key': api_key}
        url = f'{self.base_url}Misc/Cultures'
        response = requests.get(url, headers=headers)
        return response.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        headers = {'X-Api-Key': api_key}
        payload = {'number': number, 'culture': culture}
        url = f'{self.base_url}Misc/Random-Address'
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

apikey = '1342a09ae7384e94a5aa8f52febf9fa3'
obj = Misc()
print(obj.get_cultures(apikey))
print(obj.get_random_address(apikey, 5))
print(obj.get_random_address(apikey, 5, 'de'))