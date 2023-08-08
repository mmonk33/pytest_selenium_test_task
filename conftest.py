import json

import pytest
import undetected_chromedriver as ucd


@pytest.fixture(scope='class')
def data_file():
    with open('configs/base_url.txt', 'r') as f:
        base_url = f.read().splitlines()
    return base_url


@pytest.fixture(scope='class')
def data_json():
    with open('configs/base.json', 'r') as f:
        json_object = json.load(f)
        base_url = json_object['base_url']
    return base_url


@pytest.fixture(scope="session")
def browser():
    driver = ucd.Chrome()
    yield driver
    driver.quit()


