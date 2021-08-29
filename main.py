from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome()
driver.get('https://soundcloud.com/nocopyrightsounds')
driver.implicitly_wait(10)

cookies_button = driver.find_element_by_id('onetrust-accept-btn-handler')
cookies_button.click()
driver.implicitly_wait(5)
driver.implicitly_wait(30)

elements = driver.find_elements_by_class_name('soundList__item')
for element in elements:
    main = element.find_element_by_class_name('soundTitle__title')
    print(main.text)
    print(main.get_attribute('href'))
print(elements)


def scroll():
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(30)
    elements = driver.find_elements_by_class_name('soundList__item')
    return len(elements)


elements_count = 0
while elements_count < 250:
    elements_count = scroll()
    print(elements_count)

