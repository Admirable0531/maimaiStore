import requests
import csv
from bs4 import BeautifulSoup
import urllib.parse
from dotenv import load_dotenv
import os
load_dotenv()

# Function to geocode an address using Google Maps Geocoding API
def geocode_address(address):
    api_key = os.getenv('GOOGLE_API')
    encoded_address = urllib.parse.quote(address, safe='')
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={encoded_address}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None

# URL of the website to scrape
url = "https://location.am-all.net/alm/location?gm=96&ct=1000&at=0"

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the response with the correct encoding
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding=response.encoding)

    # Find all <span class="store_name"> and <span class="store_address"> elements
    store_name_elements = soup.find_all("span", class_="store_name")
    store_address_elements = soup.find_all("span", class_="store_address")

    # Extract the text content of the <span> elements
    store_names = [element.text.strip() for element in store_name_elements]
    addresses = [element.text.strip() for element in store_address_elements]

    # Initialize a list to store the data
    data = []

    # Geocode each address to get its coordinates
    for store_name, address in zip(store_names, addresses):
        lat, lng = geocode_address(address)
        data.append((store_name, address, lat, lng))

    # Write data to a CSV file with utf-8-sig encoding
    with open('store_data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Store Name', 'Address', 'Latitude', 'Longitude'])
        writer.writerows(data)

    print("Done")
else:
    print("Failed to retrieve the website content.")