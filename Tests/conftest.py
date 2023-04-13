"""
1.driver initialization
2.launching the website
3.close the webpage
"""
import pytest
from selenium import webdriver
from Library.config import Config


@pytest.fixture()
def driver_init():
    if Config.BROWSER_NAME.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Config.CHROMEDRIVER_PATH)

    elif Config.BROWSER_NAME.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=Config.GECKODRIVER_PATH)

    else:
        driver = webdriver.Edge(executable_path=Config.EDGEDRIVER_PATH)

    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    driver.close()