from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome()
driver.get('http://www.python.org')
assert 'Python' in driver.title
