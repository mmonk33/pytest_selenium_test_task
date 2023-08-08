import pytest
import undetected_chromedriver as ucd


@pytest.fixture(scope='session')
def data_file():
    with open('base_url.txt', 'r') as f:
        data = f.read().splitlines()
    return data


@pytest.fixture(scope="session")
def browser():
    driver = ucd.Chrome()
    yield driver
    driver.quit()


