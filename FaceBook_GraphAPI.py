import requests
import json

url = "https://graph.facebook.com/v15.0/1735865233097334?fields=link%2Cimages&access_token=EAAF3ZCBMyOCYBAFzUCpTMibB5RMWZCsUSZBnE8bkZCSzKXpH8ZAVlSme9kZCgTIqfxOEcpZAZA2cMTfM3iLRzjJdtNrZBt7VSZAaw3lBBHhj5Ju4W7ZAIbx8JCHIgMCNtYvRNk84PV3rw4ntUwegTNHsvZAZAksvxWOvmIoED16QLpWH6cVvoZCYr3OjbZAZCjyW6HeDRfQ7fWfniZA2vV7QvaZA7VtCGYu4G7yZCcBTZAoSZAUJwIeXMzCJ1zN9nkvl7"

response = requests.get(url)
data = response.text
data = json.loads(data)

image_url = data['images'][0]['source']

image_bytes = requests.get(image_url).content

with open('image.jpg', 'wb') as file:
  file.write(image_bytes)
