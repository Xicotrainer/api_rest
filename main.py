import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    arg = {
        'name': 'Ramanujan',
        'course': 'api_rest',
        'level': 'basic'
    }

    response = requests.post(url, params=arg)
    
    if response.status_code == 200:
        response_json = json.loads(response.text)
        response_json = json.dumps(response_json, indent=2)

        print(response.url, response_json, end='\n')