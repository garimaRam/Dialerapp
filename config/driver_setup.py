import configparser
from appium import webdriver

# Read config.ini file
config = configparser.ConfigParser()
config.read("config/config.ini")

def get_driver():
    caps = {
        "platformName": config.get("DEVICE", "platformName"),
        "deviceName": config.get("DEVICE", "deviceName"),
        "appPackage": config.get("DEVICE", "appPackage"),
        "appActivity": config.get("DEVICE", "appActivity"),
        "automationName": config.get("DEVICE", "automationName"),
        "noReset": config.getboolean("DEVICE", "noReset"),
    }

    return webdriver.Remote(config.get("APPIUM", "server_url"), caps)
