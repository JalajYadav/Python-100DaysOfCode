# ---------Rem to write Config file-------------#
import os
import requests
from twilio.rest import Client
api_key = os.environ['API_KEY']
parameter = {
    "lon": 150.5,  # 70.1333,
    "lat": -15.683333,  # 23.0833,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

will_rain = False
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its going to rain¯\_(ツ)_/¯,Take Umbrella",
        from_='<Twilio Phone Number>',
        to='<Twilio Registered>'
    )
    print(message.status)
    print(message.sid)
