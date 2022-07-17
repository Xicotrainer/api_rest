import requests
import json

def jsonify(response):
    response_json = json.loads(response.text)
    response_json = json.dumps(response_json, indent=4)  
    
    return response_json


if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {
        'name': 'Ramanujan',
        'course': 'api_rest',
        'level': 'basic'
    }
    headers = {
        'Conten-Type': 'application/json',
        'access-token': '12345'
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print(response.url)
        print(jsonify(response))
        print(response.headers['Server'])