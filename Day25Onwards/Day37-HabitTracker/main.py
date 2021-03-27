import requests
import os
from datetime import datetime

USERNAME = os.environ['<your unique userame lower case necessary>']  # no need to preregister this
TOKEN = os.environ['<your unique token>']  # no need to preregister this
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "SkippingRope",
    "unit": "Skips",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()
# today = datetime(year=2021, month=1, day=22)
# print(today.strftime("%Y%m%d"))
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Skips did u do today: ")
}
# response = requests.post(url=pixel_creation_endpoint,json=pixel_config,headers=headers)
# print(response.text)


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

update_pixel_config = {
    "quantity": "500"
}

# response = requests.put(url=update_pixel_endpoint,json=update_pixel_config,headers=headers)
# print(response.text)


delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)
