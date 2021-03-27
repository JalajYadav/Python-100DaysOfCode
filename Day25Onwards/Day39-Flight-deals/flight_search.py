import os

api_header = {
    "apikey": os.environ["<Your Api Header for Tequila Flights Api>"]
}
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

import requests
from pprint import pprint
from flight_data import FlightData


class FlightSearch:

    def destination_code(self, city_name):
        query = {
            "term": f"{city_name}",
            "locale": "en - US",
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query",
                                headers=api_header,
                                params=query)
        response = response.json()
        return response["locations"][0]["code"]

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        query = {
            "fly_from": f"{origin_city_code}",
            "fly_to": f"{destination_city_code}",
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                headers=api_header,
                                params=query)
        response = response.json()
        # pprint(response)
        try:
            data = response["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                    headers=api_header,
                                    params=query)
            response = response.json()
            try:
                data = response["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None
            else:
                # pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: Rs.{flight_data.price}")
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: Rs.{flight_data.price}")
            return flight_data
