import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        headers = {'X-Api-Key': api_key}
        url = f'{self.base_url}SocialNumber'
        response = requests.get(url, headers=headers)
        return response.json()

apikey = '1342a09ae7384e94a5aa8f52febf9fa3'
obj = SocialNumber()
print(obj.get_SocialNumber(apikey))
