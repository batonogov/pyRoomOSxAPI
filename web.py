from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Запрос перечня ссылок на группы комманд
def xapi_cmd(url='https://roomos.cisco.com/xapi?Product=hopen', output_file_name=None):
    with open(f'pyRoomOSxAPI/{output_file_name}', 'w') as f:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(1)
        reference = [c for c in driver.find_element(By.CLASS_NAME, 'sub-menu').text.split('\n')]
        driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(2)").click()
        for i in range(len(reference)):
            driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
            command_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
            f.write(f'class {reference[i].replace(" ", "_").replace("(", "").replace(")", "")}:\n')
            f.write(f'    def __init__(self) -> str:\n        pass\n\n')
            temp = []
            for i in range(len(command_line)):
                driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Command.{command_line[i]}/")]').click()

                try:
                    driver.find_element(By.CLASS_NAME, 'switcher').click()
                    switcher = driver.find_element(By.CLASS_NAME, 'language-javascript').text.split()
                    print(len(switcher), f'{switcher}\n')
                    name = switcher[2]
                    if len(switcher) == 4:
                        if name not in temp:
                            temp.append(name)
                            f.write(f'    class {name}:\n        pass\n\n')
                        f.write(f'        def {switcher[3]}():\n            pass\n\n')

                except Exception as e:
                    print(e)

                # try:
                #     info = driver.find_element(By.CLASS_NAME, 'info').text
                #     print(f'{info}\n')
                #     f.write(f'{info}\n')
                # except:
                #     pass

                # try:
                #     param = driver.find_element(By.CLASS_NAME, 'param').text
                #     print(f'{param}\n')
                #     f.write(f'{param}\n')
                # except:
                #     pass

                # try:
                #     props = driver.find_element(By.CLASS_NAME, 'props').text
                #     print(f'{props}\n')
                #     f.write(f'{props}\n')
                # except:
                #     pass

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
            
xapi_cmd(output_file_name='xCommand.py')
