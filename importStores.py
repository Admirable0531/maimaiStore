#!/Users/USER/AppData/Local/Programs/Python/Python312/python.exe
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://location.am-all.net/alm/location?gm=96&ct=1000&at=0"

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <span class="store_address"> elements
    store_address_elements = soup.find_all("span", class_="store_address")

    # Extract the text content of the <span> elements and format them as JavaScript strings
    addresses = [f'"{element.text.strip()}"' for element in store_address_elements]

    # Format the addresses as a JavaScript array
    js_addresses = "var addresses = [\n" + ",\n".join(addresses) + "\n];"

    # Print the JavaScript array
    print(js_addresses)
else:
    print("Failed to retrieve the website content.")