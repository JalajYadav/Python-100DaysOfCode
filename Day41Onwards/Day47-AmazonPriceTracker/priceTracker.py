import os

email_id = os.environ["<Your Email Id>"]
email_pass = os.environ["<Your Email Password>"]

product_name = "Apple MacBook Pro (16-inch, 16GB RAM, 1TB Storage, 2.3GHz 9th Gen Intel Core i9)"
product_url = "https://www.amazon.in/Apple-MacBook-16-inch-Storage-2-3GHz/dp/B081JWZSSX/ref=sr_1_3?dchild=1&keywords=macbook+pro&qid=1617269321&sr=8-3"
product_threshold_price = 240000

import requests
from bs4 import BeautifulSoup
import smtplib

# if u do not have lxml package installed then uncomment the line below and install the package
# import lxml




response = requests.get(url=product_url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'})
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")
price = soup.find(name="span", class_="priceBlockBuyingPriceString").getText()
price = price.split("\xa0")[1]
price = price.split(".")[0]
price = price.split(",")
final_price = 0

for i in range(len(price) - 2, -1, -1):
    final_price += ((int(price[i]) * 1000) * (100 ** ((len(price) - 2) - i)))
final_price += int(price[-1])

if product_threshold_price > final_price:
    message = f"Price of the product {product_name} has dropped from {product_threshold_price} to {final_price} today,\n" \
              f"so here is the link if u wish to buy>>>>>> \n {product_url}"
    message.encode('utf-8')
    print(message)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_id, password=email_pass)
        connection.sendmail(
            from_addr=email_id,
            to_addrs="<Receiver@gmail.com>",
            msg=f"Subject:Price Drop Alert\n\n{message}")
