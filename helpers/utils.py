from selenium.webdriver import Chrome, Edge, Firefox


def drivers(name):
    driver = {
        'Chrome': Chrome,
        'Edge': Edge,
        'Firefox': Firefox
    }
    return driver[name]