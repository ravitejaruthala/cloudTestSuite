from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = None

def close_browser():
    global driver
    driver.close()
    
def click(locator):
    global driver
    driver.find_element(By.XPATH, locator).click()

def launch_browser(browserName):
    global driver
    match browserName:
        case 'chrome':
            driver = webdriver.Chrome()
        case 'firefox':
            driver = webdriver.Firefox()
def navigate_to_page(url):
    global driver
    driver.get(url)
    driver.maximize_window()
    
def send_keys(locator, input):
    global driver
    driver.find_element(By.XPATH, locator).send_keys(input)
    
