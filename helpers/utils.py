from selenium.webdriver import Chrome, Firefox, ChromiumEdge


def drivers(name):
    driver = {
        'Chrome': Chrome,
        'Edge': ChromiumEdge,
        'Firefox': Firefox
    }
    return driver[name]