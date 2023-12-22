from pytest import fixture



def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default='Chrome', help="Browser options [Chrome, Edge, Firefox]")


@fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")
