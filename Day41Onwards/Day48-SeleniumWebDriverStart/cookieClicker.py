from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

time_add_on = time.time() + 5
exit_time = time.time() + 300

cookie = driver.find_element_by_id('cookie')

keep_going = True

while keep_going:
    cookie.click()

    # ---exit after 5 minutes--#
    if time.time() >= exit_time:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        driver.quit()
        keep_going = False
        break

    # ----buy after 5 seconds----#
    if time.time() >= time_add_on:
        time_add_on = time.time() + 5

        # buy_options = driver.find_elements_by_css_selector('#store div')
        # buy_options.pop()
        buy_options = driver.find_elements_by_xpath('//div[starts-with(@id, "buy")]')
        buy_options.pop()  # actually, I'm not sure you need this - not tested

        items_prices = [price.text for price in driver.find_elements_by_css_selector('#store div b')]
        items_prices.pop()
        items_prices = [int(item.split("- ")[1].replace(",", "")) for item in items_prices]

        for item_price in reversed(items_prices):

            try:
                money_available = int(driver.find_element_by_id('money').text.replace(",", ""))

                if item_price <= money_available:
                    # buy_options = driver.find_elements_by_xpath('//div[starts-with(@id, "buy")]')
                    # buy_options.pop()
                    buy_options[items_prices.index(item_price)].click()
                    # time.sleep(0.1)
                    break  # only buying one item per cycle

                # else:  # not required
                #     continue
            except StaleElementReferenceException as e:
                print(e)


