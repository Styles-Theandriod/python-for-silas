import requests

def download_image(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f'Image downloaded successfully to {destination}')
    else:
        print(f'Image download failed. status: {response.status_code}')

image_url = 'https://picsum.photos/300/300'
destination_path = 'image/image.jpg'

download_image(image_url, destination_path)