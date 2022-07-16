import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    arg = {
        'name': 'Ramanujan',
        'course': 'api_rest',
        'level': 'basic'
    }

    response = requests.get(url, params=arg)
    
    if response.status_code == 200:
        """
        response_json = response.json()
        print(response.url, response_json['origin'], end='\n')

        """
        response_json = json.loads(response.text)
        print(response_json['origin'])