import pytest
from selenium.webdriver.common.by import By


def test_have_button_bay(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    assert button