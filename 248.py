from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests,time,math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser.get(link)
    price = WebDriverWait(browser,15).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    btn = browser.find_element_by_css_selector('#book')
    btn.click()
    x = browser.find_element_by_id('input_value').text
    an = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(an)
    btn2 = browser.find_element_by_id('solve')
    btn2.click()

finally:
    time.sleep(10)
    browser.quit()



