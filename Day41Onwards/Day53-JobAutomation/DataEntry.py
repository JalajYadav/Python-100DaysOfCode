Google_form_link = 'https://forms.gle/9GHcJXfcL8HvDArr9'
Zillow_property_link = 'https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A1386301%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A4500%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'


from bs4 import BeautifulSoup
import requests

response = requests.get(Zillow_property_link,headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
})
webpage = response.text

soup = BeautifulSoup(webpage,'html.parser')
#print(soup)
price_list = [item.getText() for item in soup.find_all(name='div',class_='list-card-price')]

direct_links_list=[]
for item in soup.find_all(name='a',class_='list-card-link'):
    link = item.get('href')
    if link.find("www.zillow.com") == -1:
        direct_links_list.append(f'https://www.zillow.com{link}')
    else:
        direct_links_list.append(link)

address_list = [item.getText() for item in soup.find_all(name='address',class_='list-card-addr')]

# ----------------------------selenium for filling details in google form----------------------------#
from selenium import webdriver
from time import sleep
chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

for i in range(0,len(price_list)):
    driver.get(Google_form_link)
    sleep(2)
    print(f"{i}-{price_list[i]}\n{i}-{address_list[i]}\n{i}-{direct_links_list[i*2]}")

    address_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(f'{address_list[i]}')
    sleep(1)
    price_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(f'{price_list[i]}')
    sleep(1)
    direct_link_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    direct_link_input.send_keys(f'{direct_links_list[i*2]}')
    sleep(1)
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    sleep(2)