INSTAGRAM_EMAIL_ID = '<<<<<<<Your Ig email id>>>>>>>>>>'
INSTAGRAM_PASSWORD = '<<<<<<<Your Ig password>>>>>>>>>>'

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep


chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.instagram.com/accounts/login/')

sleep(3)
user_id = driver.find_element_by_name('username')
user_id.send_keys(INSTAGRAM_EMAIL_ID)

user_pass = driver.find_element_by_name('password')
user_pass.send_keys(INSTAGRAM_PASSWORD)

login_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]')
login_btn.click()
sleep(5)
not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
not_now.click()
sleep(2)

search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]')
search.click()
sleep(1)

search_input = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
search_input.send_keys('freecodecamp')
sleep(2)
first_result = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]')
first_result.click()
sleep(2)

followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
followers.click()
sleep(2)

follower_list = driver.find_elements_by_css_selector('div.PZuss li button')

follower_round = 1
while follower_round!=3:# here you can decide the number of rounds each round is for approx. 11 followers
    print('Round: ', follower_round)
    for i in range(0,len(follower_list)):
        print(f'Following follower no. {i}')
        try:
            follower_list[i].click()
            sleep(2)
        except ElementClickInterceptedException:
            cancel= driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
            cancel.click()

    follower_list=driver.find_elements_by_css_selector('div.PZuss li div.Pkbci button.y3zKF')
    follower_round+=1


print('Code ends Now')
