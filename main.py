import requests
import json

def jsonify(response):
    response_json = json.loads(response.text)
    response_json = json.dumps(response_json, indent=4)  
    
    return response_json


if __name__ == '__main__':
    url = 'https://httpbin.org/delete'
    payload = {
        'name': 'Ramanujan',
        'course': 'api_rest',
        'level': 'basic'
    }
    headers = {
        'Conten-Type': 'application/json',
        'access-token': '12345'
    }

    response = requests.delete(url, data=json.dumps(payload), headers=headers)

    # This is the CRUD methods for http:
        # GET. To abtain a resource item
        # POST. To create a resource item
        # PUT. To update a resource item
        # DELETE. To remove a resource item
    
    if response.status_code == 200:
        print(response.url)
        # print(jsonify(response))
        print(response.headers['Server'])