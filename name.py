import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        headers = {'X-Api-Key': api_key}
        payload = {'nameType': nameType, 'quantity': quantity}
        url = f'{self.base_url}Name'
        response = requests.get(url, headers=headers, params=payload)
        return response.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        headers = {'X-Api-Key': api_key}
        payload = {'startingWords': startingWords}
        url = f'{self.base_url}Name/Suggestions'
        response = requests.get(url, headers=headers, params=payload)
        return response.json()
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        headers = {'X-Api-Key': api_key}
        url = f'{self.base_url}Name/Cultures'
        response = requests.get(url, headers=headers)
        return response.json()

apikey = '1342a09ae7384e94a5aa8f52febf9fa3'
obj = Name()
# print(obj.get_name(api_key=apikey, nameType='firstname', quantity=1))
# print(obj.get_name_suggestions(api_key=apikey, startingWords='john'))
# print(obj.get_name_cultures(apikey))