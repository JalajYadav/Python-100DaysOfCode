import requests
import datetime as dt
import smtplib
import time
#------------iss api----------------#
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat=float(data["iss_position"]["latitude"])
iss_lng=float(data["iss_position"]["longitude"])
print("Iss latitude",iss_lat)
print("Iss longitude",iss_lng)

#-------------------my sunrise time---------------#

my_lat=23.064739
my_lng=70.129860
parameter ={
    "lat":my_lat,
    "lng":my_lng,
    "formatted":0
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data= response.json()
#print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])+5
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])+5

print("sunrise",sunrise,"sunset",sunset)

time_now = dt.datetime.now()
print("Current HRS",time_now.hour)


# ------------------comparator function if iss is in my latitude region-------------------#
def comparator():
    if my_lat - 5 <= iss_lat <= my_lat + 5 and my_lng - 5 <= iss_lng <= my_lng + 5:
        return True

# ----------------comparator function to check if it is night or day-----#
def night_day_comp():
    if sunrise <= time_now.hour <= sunset:
        return True
while True:
    time.sleep(60)
    if comparator() and night_day_comp():
        print("Loookup to the sky")
        # my_mail = "<Your mail address>"
        # my_pass = "<Your password>"
        # with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        #     connection.starttls()
        #     connection.login(user=my_mail,password=my_pass)
        #     connection.sendmail(
        #         from_addr=my_mail,
        #         to_addrs="<ReceiversMail>",
        #         msg="Subject:Lookup\n\nThe ISS is above you"
        #     )

