import requests

if __name__ == '__main__':
    url = 'https://i.imgur.com/cK64mEv.jpeg'
    
    response = requests.get(url, stream=True) #Make the request without downloading the content
    with open('doggy_image.jpg', 'wb') as file:
        for chunk in response.iter_content(): # Download the contentent by segments
            file.write(chunk)

    response.close()