from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

artile_count = driver.find_element_by_css_selector("#articlecount a")
print(artile_count.text)

# all_portals=driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name('search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)

# driver.quit()

#----mini challenge-----#
# driver.get('https://secure-retreat-92358.herokuapp.com/')
# fname = driver.find_element_by_name('fName')
# fname.send_keys('Python')
# lname = driver.find_element_by_name('lName')
# lname.send_keys('Selenium')
# email = driver.find_element_by_name('email')
# email.send_keys('haeeyaah@yahoo.in')
# import  time
# time.sleep(5)
# sign_up = driver.find_element_by_tag_name('button')
# sign_up.click()
# driver.quit()