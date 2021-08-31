from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary  # Adds chromedriver binary to path


class Song:
    def __init__(self, title: str, plays: str, comments: str, link: str):
        self.title = title
        self.plays = plays
        self.comments = comments
        self.link = link

    def __str__(self):
        return f'{self.title}\n plays: {self.plays}, comments: {self.comments}\n'


driver = webdriver.Chrome()
driver.get('https://soundcloud.com/nocopyrightsounds')
driver.implicitly_wait(10)

cookies_button = driver.find_element_by_id('onetrust-accept-btn-handler')
cookies_button.click()
driver.implicitly_wait(5)
driver.implicitly_wait(30)
sounds_element = driver.find_elements_by_class_name('soundList')
elements = sounds_element[1].find_elements_by_class_name('soundList__item')


def scroll():
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(30)
    elements = sounds_element[1].find_elements_by_class_name('soundList__item')
    return elements


while len(elements) < 10:
    elements = scroll()
    print(len(elements))

songs = []
for element in elements:
    title = element.find_element_by_class_name('soundTitle__title')
    link = title.get_attribute('href')
    stats = element.find_element_by_class_name('soundStats')
    stats = stats.find_elements_by_class_name('sc-ministats-item')
    songs.append(Song(title.text, stats[0].get_attribute('title'), stats[1].get_attribute('title'), link))
print(elements)
for song in songs: print(song)
