import requests
from datetime import datetime
parameters = {
    "lat": 12.971599,
    "log": 77.594566,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset=data["results"]["sunset"]
time_now = datetime.now()
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
print(time_now.hour)
