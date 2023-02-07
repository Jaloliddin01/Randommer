import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        headers = {'X-Api-Key': api_key}
        url = f'{self.base_url}Card'
        payload = {'type': type} if type else None
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        url = f'{self.base_url}Card/Types'
        response = requests.get(url, headers={'X-Api-Key': api_key})
        return response.json()

obj = Card()
print(obj.get_card('1342a09ae7384e94a5aa8f52febf9fa3'))
print(obj.get_card_types('1342a09ae7384e94a5aa8f52febf9fa3'))