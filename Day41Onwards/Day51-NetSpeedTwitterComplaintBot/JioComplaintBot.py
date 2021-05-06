TWITTER_EMAIL_ID = '<<<<<Your Email for Twitter>>>>>>'  # dummy account created with temp mail
TWITTER_PASSWORD = '<<<<<Your Password for Twitter>>>>>>'
AVERAGE_DOWN_SPEED = 19.3 # average speed of reliance jio as of 2020
AVERAGE_UP_SPEED = 4.6
chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"

from selenium import webdriver
from time import sleep


class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        sleep(100)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print('Download Speed: ',self.down,'\nUpload Speed: ',self.up)

    def tweet_to_provider(self):
        self.driver.get('https://twitter.com/?lang=en')
        sleep(10)
        login_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div')
        login_btn.click()

        sleep(2)
        email_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email_box.click()
        email_box.send_keys(TWITTER_EMAIL_ID)
        password_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password_box.click()
        password_box.send_keys(TWITTER_PASSWORD)
        login_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login_btn.click()
        sleep(5)

        # after logged in
        tweet_start = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]')
        tweet_start.click()
        tweet_box = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span')
        tweet_box.send_keys(f'Hello @reliancejio, please tell me why do i get {self.down}mbps download and {self.up}mbps upload speed, if the average speed is {AVERAGE_DOWN_SPEED}mbps down and {AVERAGE_UP_SPEED}mbps up...please explain...')

        tweet_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div')
        tweet_btn.click()
        print('Complaint Tweeted Successfully')
        self.driver.quit()

bot = InternetSpeedTwitterBot(driver_path=chrome_driver_path)
bot.get_internet_speed()
bot.tweet_to_provider()


