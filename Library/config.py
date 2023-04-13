"""contains configuarations required by the project"""


class Config:
    CHROMEDRIVER_PATH = r"../drivers/chromedriver.exe"
    GECKODRIVER_PATH = "../drivers/geckodriver.exe"
    EDGEDRIVER_PATH = "../drivers/msedgedriver.exe"
    LOCATORS_FILE_PATH = r"../files/Actitime_locators.xlsx"
    LOGIN_SHEET_NAME = "LoginPageObjects"
    URL = "https://demo.actitime.com/login.do"
    BROWSER_NAME = "chrome"

