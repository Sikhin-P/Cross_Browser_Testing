from selenium.webdriver import Chrome, Edge, Firefox, Safari


def drivers(name):
    driver = {
        'Chrome': Chrome,
        'Edge': Safari,
        'Firefox': Firefox
    }
    return driver[name]