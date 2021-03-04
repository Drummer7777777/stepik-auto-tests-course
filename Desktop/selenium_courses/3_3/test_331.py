from selenium import webdriver
import pytest, time, requests



link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'

browser = webdriver.Chrome()



def test_reg1():
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration1.html')
    input1 = browser.find_element_by_class_name("first")
    input1.send_keys("Vladimir")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Ponomarev")
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("asdad")
    time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!"==welcome_text, 'Ошибка регистрации'
    time.sleep(5)

def test_reg2():
    browser.get(link2)
    input1 = browser.find_element_by_class_name("first")
    input1.send_keys("Vladimir")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Ponomarev")
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("asdad")
    time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!"== welcome_text, 'Ошибка регистрации'
    time.sleep(5)
    browser.quit()

#test_reg1()
#test_reg2()
#if __name__ == '__main__':
#    pytest.main()
