from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=2477932402&f_AL=true&keywords=sales%20manager')

Sign_in_btn = driver.find_element_by_link_text('Sign in')
Sign_in_btn.click()
time.sleep(2)
username = driver.find_element_by_id('username')
username.send_keys('felemov745@tripaco.com') #dummy email account created bt temp mail

password = driver.find_element_by_id('password')
password.send_keys('felemov745')

Sign_in_btn = driver.find_element_by_css_selector('button.btn__primary--large')
Sign_in_btn.click()


time.sleep(3)

all_listings = driver.find_elements_by_class_name("jobs-search-results__list-item")

for listing in all_listings:
    print("List Item")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(3)

        # If phone field is empty, then fill your phone number.
        dropdown = driver.find_element_by_css_selector('.fb-dropdown__select')
        dropdown.click()
        # in order to select United Kingdom in phone dropdown
        option = driver.find_elements_by_css_selector('.fb-dropdown__select option')
        option[-15].click()


        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys('999999')

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
            print('Successfully applied')

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

