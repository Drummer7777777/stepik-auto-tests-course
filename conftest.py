import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', default='es')

@pytest.fixture(scope='session')
def browser(request):
    language = request.config.getoption('--language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    instance_browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    yield instance_browser
    instance_browser.quit()
