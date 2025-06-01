import os, requests, random
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("apiKey")

year = random.randint(2013, 2025)
month = random.randint(1, 12)
day = random.randint(1, 28)

lat = round(random.uniform(-60, 60), 4)
lon = round(random.uniform(-180, 180), 4)
dim = round(random.uniform(0.1, 0.5), 2)

date = f"{year}-{month:02}-{day:02}"

url = f"https://api.nasa.gov/planetary/earth/assets?lon={lon}&lat={lat}&date={date}&dim={dim}&api_key={apiKey}"

response = requests.get(url)
data = response.json()

if "url" in data:
    print("Date:", data["date"])
    print("Lat:", lat, "Lon:", lon)
    print("Image URL:", data["url"])

    image_response = requests.get(data["url"])
    with open("earth_image.png", "wb") as f:
        f.write(image_response.content)
    print("Image downloaded as earth_image.png")

elif "msg" in data:
    print("NASA message:", data["msg"])
else:
    print("No image found.")
