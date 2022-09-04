'''Data colector'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm


# Генератор стукруты из списка
def generator(data, file, indent = ' ' * 4):
    '''Generate data from xapi and write data to file'''
    for i in range(len(data[1:])):
        compare = i+1 != len(data[1:])
        name = data[i+1]
        if compare and name not in TEMP:
            file.write(f'{indent * i}class {name}:\n{indent * i}    pass\n\n')
        elif not compare and name not in TEMP:
            file.write(f'{indent * i}def {name}():\n{indent * i}    pass\n\n')
        TEMP.append(name)

# Запрос перечня ссылок на группы комманд
def xapi_cmd(url='https://roomos.cisco.com/xapi?Product=hopen', output_file_name=None):
    '''Get links on command groups'''
    global TEMP
    TEMP = []
    with open(f'pyRoomOSxAPI/{output_file_name}', 'w', encoding='utf-8') as file:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(1)

        # Пакуем группы команд
        reference = driver.find_element(By.CLASS_NAME, 'sub-menu').text.split('\n')

        # Перебор xCommand
        driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(2)").click()
        for i in tqdm(enumerate(reference)):
            driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i[0]]}")]').click()
            command_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
            for j in enumerate(command_line):
                driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Command.{command_line[j[0]]}/")]').click()

                try:
                    driver.find_element(By.CLASS_NAME, 'switcher').click()
                    switcher = driver.find_element(By.CLASS_NAME, 'language-javascript').text.split()

                    colon_finder = [c for c in range(len(switcher)) if ':' in switcher[c]]

                    if colon_finder:
                        swither_slice = switcher[:colon_finder[0]]
                        generator(swither_slice, file)
                    else:
                        generator(switcher, file)

                except Exception as exception:
                    print(exception)

                # try:
                #     info = driver.find_element(By.CLASS_NAME, 'info').text.split()
                #     print(len(info), f'{info}\n')
                #     f.write(f"        '''\n            {' '.join(info)}\n        '''\n")
                # except Exception as e:
                #     print(e)

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

    # # Перебор xConfiguration
    # driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(3)").click()
    # for i in range(len(reference)):
    #     driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
    #     cfg_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
    #     for i in range(len(cfg_line)):
    #         driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Configuration.{cfg_line[i]}/")]').click()
    # # Перебор xStatus
    # driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(4)").click()
    # for i in range(len(reference)):
    #     driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
    #     status_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
    #     for i in range(len(status_line)):
    #         driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Status.{status_line[i]}/")]').click()

    # # Перебор Event
    # driver.find_element(By.CSS_SELECTOR, "#app > div > form > div.type-buttons.filter > button:nth-child(5)").click()
    # for i in range(len(reference)):
    #     driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/domain/?domain={reference[i]}")]').click()
    #     event_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
    #     for i in range(len(event_line)):
    #         driver.find_element(By.XPATH, f'//a[contains(@href,"/xapi/Event.{event_line[i]}/")]').click()

xapi_cmd(output_file_name='xCommand.py')
