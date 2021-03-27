import os

App_id = os.environ['App_id']
App_key = os.environ['App_key']


Shetty_user = os.environ['Shetty_user']
Shetty_pass = os.environ['Shetty_pass']


SheetsApi_endpoint = os.environ['SheetsApi_endpoint']
# ----------------https://developer.nutritionix.com/--------------------#
import requests

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_post_jsonData = {
    "query": input("What and How long did u exercises: "),
    "gender": "male",
    "weight_kg": 80.0,
    "height_cm": 173.00,
    "age": 20
}

headers = {
    "x-app-id": App_id,
    "x-app-key": App_key
}

response = requests.post(url=nutritionix_endpoint,json=nutritionix_post_jsonData,headers=headers)
response.raise_for_status()
print("nutritionix.com",response.status_code)
data = response.json()
execise_list = data["exercises"]




# ----------------------------https://sheety.co/----------------------#
from datetime import datetime
today = datetime.now()

headers_sheet ={
    "Content-Type":"application/json"
}
for exercise in execise_list:
    sheet_post_jsonData = {
        "workout": {
            "date": f"{today.strftime('%d/%m/%Y')}",
            "time": f"{today.strftime('%X')}",
            "exercise": f"{exercise['name'].title()}",
            "duration": f"{exercise['duration_min']}",
            "calories": f"{exercise['nf_calories']}"
        }
    }
    sheet_response = requests.post(url=SheetsApi_endpoint,
                             json=sheet_post_jsonData,
                             headers=headers_sheet,
                             auth=(Shetty_user, Shetty_pass)
                             )
    sheet_response.raise_for_status()
    print("api.sheety.co",sheet_response.status_code)


