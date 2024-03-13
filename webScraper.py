import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def image_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image elements with a specific class or ID (adjust based on the website structure)
        images = soup.find_all('img')  # You can further filter based on class or other attributes

        # Extract and print the image IDs from the image URLs
        for image in images:
            image_url = image['src']  # Replace 'src' with the actual attribute containing the image URL
            image_id = parse_qs(urlparse(image_url).query).get('id')  # Replace 'id' with the actual parameter name
            if image_id:
                print(f"Image ID: {image_id[0]}, Image URL: {image_url}")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Replace 'https://example.com' with the actual URL of the website you want to scrape
url_to_scrape = 'https://ng.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/52/{0216482}/1.jpg?3445'
image_web_scraper(url_to_scrape)
