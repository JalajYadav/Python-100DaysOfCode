from selenium import webdriver

chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# to open a web page in chrome tab
driver.get("https://www.python.org/")
element =driver.find_element_by_id("downloads")
print(element.text)

search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

docs_link = driver.find_element_by_css_selector(".documentation-widget a")
print(docs_link.text)

bug_path = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_path.text)

# All the find queries work on multiple elements as well
# just use find_elements instead.............

# to close the webpage
# driver.close()
# to quit the web browser
driver.quit()