from selenium import webdriver

chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.python.org/')


years=[item.text for item in driver.find_elements_by_css_selector("div.event-widget span")]
print(years)
dates =[item.text for item in driver.find_elements_by_css_selector("div.event-widget time")]
print(dates)
event =[item.text for item in driver.find_elements_by_css_selector("div.event-widget li a")]
print(event)

result={}
for i in range(len(event)):
    sub_dict={"Date":f"{years[i]}{dates[i]}","Events":f"{event[i]}"}
    result[i]=sub_dict
print(result)


driver.quit()