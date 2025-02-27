import requests
import json

# Define the API URL and your API Key
API_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"
API_KEY = "xidJCQRFB4RNQPM4LeqV4SZ4p1a8ic9CsCJa9ezk`"  # Replace with your NASA API key

# Make a request to the NASA API to get the latest Mars photos from Curiosity
params = {
    'api_key': API_KEY
}

# Send GET request
response = requests.get(API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # If there are photos available, print the latest ones
    if data['photos']:
        print("Latest Photos from Mars (Curiosity Rover):\n")
        for photo in data['photos']:
            print(f"Image ID: {photo['id']}")
            print(f"Sol (Mars Day) Taken: {photo['sol']}")
            print(f"Camera: {photo['camera']['name']}")
            print(f"Image URL: {photo['img_src']}\n")
    else:
        print("No photos available.")
else:
    print(f"Error fetching data from NASA API: {response.status_code}")

