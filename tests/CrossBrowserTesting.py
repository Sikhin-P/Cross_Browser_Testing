from helpers.utils import drivers


def test_google(browser):

    driver = drivers(browser)()
    driver.get('https://google.com')
