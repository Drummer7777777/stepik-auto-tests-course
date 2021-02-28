from selenium import webdriver
import requests

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/cats.html'

try:
    browser.find_element_by_id("button")

finally:
    browser.quit()
