import requests
import os
from twilio.rest import Client

api_key = "7bd040518890b29b715c2823a1659fae"
endpoint = "https://api.openweathermap.org/data/2.5/weather"
lat = "38.2527"
lon = "85.7585"


weather_params = {
	"lat": lat,
	"lon": lon,
	"appid": api_key,
	"exclude": "current,minute,daily"
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)

weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]
print(condition_code)

will_rain = False

if condition_code >= 200 and condition_code <= 531:
	will_rain = True




# ----------------------- TWILLO SMS SECTION -------------------

account_sid = ""
auth_token = ""


if will_rain:
	client = Client(account_sid, auth_token)

	message = client.messages.create(
		body="It's going to rain today.",
		from_="+12058557374",
		to=""
	)
	print(message.status)




