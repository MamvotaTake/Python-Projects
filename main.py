import random
import smtplib
from datetime import datetime

import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

api_key = ""
weather_parameters = {
    "lat": ,
    "lon": ,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

my_email = ""
password = ""

response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True
# weather_slice = weather_data["hourly"][0]["weather"][0]["id"]
with open("quotes.txt") as quotes_file:
    quotes_list = quotes_file.readlines()
    quote = random.choice(quotes_list)
    print(quote)

name = "CEO"
today = datetime.now()
hour = today.hour
#for gmail (smtp.gmail.com)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if will_rain:

        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Rain Alert\n\n{name} Take bring an umbrella it will be raining today\n{quote}")
    else:

        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Rain Alert\n\n{name} Take No rain today\n{quote}")
