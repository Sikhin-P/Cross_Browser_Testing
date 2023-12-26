from selenium.webdriver import Chrome, Firefox


def drivers(name):
    driver = {
        'Chrome': Chrome,
        'Edge': Chrome,
        'Firefox': Firefox
    }
    return driver[name]