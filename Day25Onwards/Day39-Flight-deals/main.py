# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.getData()

# ------------------------iataCode and Flight Search-------------------------------#

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

ORIGIN_CITY_IATA = "DEL"  # origin city is delhi

flight_search = FlightSearch()
sms = NotificationManager()
message = ""
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.destination_code(row["city"])
        data_manager.put_iata_code(row["id"], row["iataCode"])
    # --------------run flight search for all funtions--------------------------#
    flights = flight_search.search_flights(origin_city_code=ORIGIN_CITY_IATA,
                                           destination_city_code=row["iataCode"],
                                           from_time=tomorrow,
                                           to_time=six_month_from_today
                                           )

    if flights is not None and row["lowestPrice"] > flights.price:
        message += (
            f"Only Rs.{flights.price} for flight from {flights.origin_city}-{flights.origin_airport} to {flights.destination_city}-"
            f"{flights.destination_airport}, from {flights.out_date} to {flights.return_date}\n")
        link = f"https://www.google.co.uk/flights?hl=en#flt={flights.origin_airport}.{flights.destination_airport}.{flights.out_date}*{flights.destination_airport}.{flights.origin_airport}.{flights.return_date}"
        link.encode('utf-8')
        message += f"{link}\n"
        if flights.stop_overs > 0:
            message += f"\nFlight has {flights.stop_overs} stop over, via {flights.via_city}."
print(message)



##########in order to send mail to subscribers################
# sms.send_emails(text=message,receivers_list=data_manager.subscribers())


###########in order to send twilio sms to admin################
# sms.send_message(f"Only Rs.{flights.price} for flight from {flights.origin_city}-{flights.origin_airport} to {flights.destination_city}-"
#                  f"{flights.destination_airport}, from {flights.out_date} to {flights.return_date}")
