from selenium.webdriver import Chrome, Edge, Firefox, Ie


def drivers(name):
    driver = {
        'Chrome': Chrome,
        'Edge': Ie,
        'Firefox': Firefox
    }
    return driver[name]