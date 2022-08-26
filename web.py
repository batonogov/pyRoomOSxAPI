from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time


def xapi_cmd(url='https://roomos.cisco.com/xapi?Product=hopen', wait=5):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

 # Пакуем группы команд 
    reference = [c for c in driver.find_element(By.CLASS_NAME, 'sub-menu').text.split('\n')]

 # Перебор xCommand
    driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(2)").click()
    for i in range(len(reference)):
        driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
        command_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
        for i in range(len(command_line)):
            driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Command.{command_line[i]}/")]').click()

 # Перебор xConfiguration   
    driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(3)").click()
    for i in range(len(reference)):
        driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
        cfg_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
        for i in range(len(cfg_line)):
            driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Configuration.{cfg_line[i]}/")]').click()
 # Перебор xStatus
    driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(4)").click()
    for i in range(len(reference)):
        driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
        status_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
        for i in range(len(status_line)):
            driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Status.{status_line[i]}/")]').click()

 # Перебор Event
    driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(5)").click()
    for i in range(len(reference)):
        driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
        event_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
        for i in range(len(event_line)):
            driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Event.{event_line[i]}/")]').click()

xapi_cmd()

