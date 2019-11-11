from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def before_all(context):
    context.driver = webdriver.Chrome()


def after_all(context):
    context.driver.close()