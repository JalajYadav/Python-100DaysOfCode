STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import os

# stock api
StockApi_key = os.environ['stock_apiKey']

# news api
NewsApi_key = os.environ['news_apiKey']

# --------------------------------------main------------------------------------------------#
import requests
from twilio.rest import Client

parameter_stock_price = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": StockApi_key
}
response = requests.get(url="https://www.alphavantage.co/query", params=parameter_stock_price)
response.raise_for_status()
data = response.json()
list_stock_CPrice = []
for item in data["Time Series (Daily)"]:
    list_stock_CPrice.append(data["Time Series (Daily)"][item]["4. close"])
yes_CPrice = float(list_stock_CPrice[0])
day_before_yes_CPrice = float(list_stock_CPrice[1])
# print(yes_CPrice, day_before_yes_CPrice)
dif_Cprice = abs(yes_CPrice - day_before_yes_CPrice)
percentage_drop = round((dif_Cprice / day_before_yes_CPrice) * 100, 2)
if yes_CPrice < day_before_yes_CPrice:
    symbol = "🔻"
else:
    symbol = "🔺"
print(symbol, percentage_drop)

# -------------------------first 3 news pieces for the COMPANY-------------------#

parameter_news_api = {
    "q": STOCK,
    "apiKey": NewsApi_key
}
response2 = requests.get(url="https://newsapi.org/v2/everything", params=parameter_news_api)
response2.raise_for_status()
data = response2.json()
article_slice = data["articles"][:3]

# -------------------------Sms Message-------------------#

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)
for i in range(len(article_slice)):
    message_text = f'{STOCK},{symbol},{percentage_drop},News:{article_slice[i]["title"]}'
    print(message_text)
    message = client.messages \
        .create(
        body=f'{message_text}',
        from_='<Twilio Phone Number>',
        to='<Twilio Registered>'
    )
    print(message.status)
    print(message.sid)
