import requests
from PIL import Image, ImageDraw, ImageFont

X_API_KEY = '7CwbabvMoAHHpqP1VthjiA==MAelWFXPxQ04kAXX'
URL = 'https://api.api-ninjas.com/v1/jokes'
headers = {'X-API-KEY': X_API_KEY}
response = requests.get(URL, headers=headers)
data = response.json()
joke = data[0].get('joke')


image = Image.new("RGB", (2000, 2000), color='black')
image.save("joke.jpg")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=60)
if len(data) > 63:
    data = data[:63] + "\n" + data[64:]
draw.text((100, 500), joke, color='white', font=font)
image.show()
print("And here's your joke!")