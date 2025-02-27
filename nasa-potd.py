import requests
import json

# Define the API URL and your API Key
API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "xidJCQRFB4RNQPM4LeqV4SZ4p1a8ic9CsCJa9ezk"  # Replace with your NASA API key

# Make a request to the NASA API to get the Astronomy Picture of the Day (APOD)
params = {
    'api_key': API_KEY
}

# Send GET request
response = requests.get(API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Print details about the Astronomy Picture of the Day
    print("Astronomy Picture of the Day (APOD):\n")
    print(f"Title: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Explanation: {data['explanation']}")
    print(f"Image URL: {data['url']}\n")

    # If it's a video, print the video URL
    if data['media_type'] == 'video':
        print(f"Video URL: {data['url']}")
else:
    print(f"Error fetching data from NASA API: {response.status_code}")

