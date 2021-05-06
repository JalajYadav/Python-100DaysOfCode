'''
########  ######## ##     ## ######## ##     ## ########  ######## ########
##     ## ##       ###   ### ##       ###   ### ##     ## ##       ##     ##
##     ## ##       #### #### ##       #### #### ##     ## ##       ##     ##
########  ######   ## ### ## ######   ## ### ## ########  ######   ########
##   ##   ##       ##     ## ##       ##     ## ##     ## ##       ##   ##
##    ##  ##       ##     ## ##       ##     ## ##     ## ##       ##    ##
##     ## ######## ##     ## ######## ##     ## ########  ######## ##     ##

To add in your Facebook Id username and password to login into Tinder, find it in the code below
'''
from selenium import webdriver
import time

chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://tinder.com/')

login_btn = driver.find_element_by_xpath('//*[@id="u-1554866805"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()
time.sleep(2)
more_options = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/button')
more_options.click()
time.sleep(2)
faceBook_login = driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div[1]/div/div[3]/span/div[2]/button')
faceBook_login.click()
time.sleep(3)


base_window = driver.window_handles[0]
faceBook_popUp = driver.window_handles[1]

driver.switch_to.window(faceBook_popUp)
print(driver.title)

email_box = driver.find_element_by_id('email')
email_box.send_keys('<<<<<<<<<<<Your FaceBook Email Id>>>>>>>>>>>>>')

password_box = driver.find_element_by_id('pass')
password_box.send_keys('<<<<<<<<<<<Your FaceBook Password>>>>>>>>>>>>>')

login_btn = driver.find_element_by_name('login')
login_btn.click()

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(7)
try:
    allow = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
    allow.click()
    time.sleep(1)
    disable_notification = driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div/div/div[3]/button[2]')
    disable_notification.click()
    time.sleep(5)
    accept_cookies = driver.find_element_by_xpath('//*[@id="u-1554866805"]/div/div[2]/div/div/div[1]/button')
    accept_cookies.click()
    time.sleep(1)
    no_thanks = driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div[1]/button')
    no_thanks.click()
except:
    print('Some Exception raised')

# hit Dislike as i do not want to disturb anyone
for i in range(5):
    dislike_btn = driver.find_element_by_xpath('//*[@id="u-1554866805"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
    dislike_btn.click()
    time.sleep(2)
    print(f'{i} proile')
