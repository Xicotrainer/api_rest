import requests

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    arg = {
        'name': 'Ramanujan',
        'course': 'api_rest',
        'level': 'basic'
    }

    response = requests.get(url, params=arg)
    
    if response.status_code == 200:
        print(response.url, response.content, end='\n')

        