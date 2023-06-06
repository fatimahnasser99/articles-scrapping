from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values(".env")

def extractWebsite(url, driverPath, driverType='chrome'):
    driver = None
    try:
        if driverType == 'chrome':
            driver = webdriver.Chrome(executable_path=driverPath)
        elif driverType == 'edge':
            driver = webdriver.Edge(executable_path=driverPath)
        elif driverType == 'firefox':
            driver = webdriver.Firefox(executable_path=driverPath)
        elif driverType == 'safari':
            driver = webdriver.Safari(executable_path=driverPath)
        else:
            raise ValueError(f"Unsupported driver type: {driverType}")
    except Exception as e:
        error_message = f"Failed to create driver: {str(e)}"
        print(error_message)
        return ''

    try:
        driver.get(url)
        htmlContent = driver.page_source
        driver.quit()
    except Exception as e:
        error_message = f"Failed to load URL '{url}': {str(e)}"
        print(error_message)
        return ''
    
    return htmlContent


def htmlParser(htmlContent):
    try:
        soup = BeautifulSoup(htmlContent, 'html.parser')
    except:
        print("something went wrong")
        return None
    
    return soup


def scrapping(url):
    path = config['driver_path']
    driver_type = config['driver_type']
    content = extractWebsite(url, path, driver_type)
    data = htmlParser(content)
    return data