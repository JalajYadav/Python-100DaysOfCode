from selenium import webdriver

chrome_driver_path = "E:\My Space\PyCharm_Projects\ChromeWebDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.empireonline.com/movies/features/best-movies-2/')

movie_name_element = driver.find_elements_by_css_selector('h3.jsx-4245974604')
movie_name = [item.text for item in movie_name_element]

with open('MovieList.txt',mode='w') as file:
    for item in movie_name:
        file.write(f'{item}\n')
driver.quit()