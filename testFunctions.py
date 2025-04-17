from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

# Set up headless mode for Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")

# Set up headless mode for Firefox
firefox_options = Options()
firefox_options.headless = True  # Run Firefox in headless mode

driver = None

def close_browser():
    global driver
    driver.close()
    
def click(locator):
    global driver
    driver.find_element(By.XPATH, locator).click()

def launch_browser(browserName):
    global driver
    if browserName == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    elif browserName == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
    elif browserName == 'edge':
        driver = webdriver.Edge()
def navigate_to_page(url):
    global driver
    driver.get(url)
    driver.maximize_window()
    
def send_keys(locator, input):
    global driver
    driver.find_element(By.XPATH, locator).send_keys(input)
    
