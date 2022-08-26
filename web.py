from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time


def xapi_cmd(url='https://roomos.cisco.com/xapi?Product=hopen&Type=Command', wait=5):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    reference = [c for c in driver.find_element(By.CLASS_NAME, 'sub-menu').text.split() if c.isalnum()]
    for i in range(len(reference)):
        time.sleep(1)
        driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
        command_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
        for i in range(len(command_line)):
            time.sleep(1)
            driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Command.{command_line[i]}/")]').click()
            print(driver.find_element(By.CLASS_NAME, 'props').text)
 
groups= xapi_cmd()
print(groups)

