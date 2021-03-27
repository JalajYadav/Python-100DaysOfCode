import os
Sheety_prices_URL = os.environ["<Your SheetyApi url for prices sheet>"]
###################################################
Shetty_emails_url = os.environ["<Your SheetyApi url for users email sheet>"]

import  requests
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.response = requests.get(url=Sheety_prices_URL)
        self.data = self.response.json()
    def getData(self):
        pprint(self.data)
        return self.data["prices"]

    def put_iata_code(self,id,iataCode):
        sheety_put_data ={
            "price":{
                "iataCode":f"{iataCode}"
            }
        }
        self.response = requests.put(url=f"{Sheety_prices_URL}/{id}",json=sheety_put_data)
        print(self.response.status_code,"status code for putting iata code data in Sheety")

    def subscribers(self):
        response = requests.get(url=Shetty_emails_url)
        email_list = response.json()
        return email_list['users']
