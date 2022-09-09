'''Data colector'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm


TEMP = []

# Генератор стукруты из списка
def generator(data, file, info, indent = ' ' * 4):
    '''Generate data from xapi and write data to file'''
    try:
        colon_finder = [c for c in range(len(data)) if ':' in data[c] or 'Raw' in data[c]]
        data = data[:colon_finder[0]]
    except:
        pass

    # print(data)
    TEMP.append(data)

    try:
        print('Данные:', TEMP[-1], TEMP[-2])
        print('Сравнение:', list(set(TEMP[-1]) & set(TEMP[-2])))
        print('Разность:', list(set(TEMP[-1]) ^ set(TEMP[-2])), '\n')
    except:
        pass

    for i in enumerate(data[1:]):
        name = i[1]
        # print(i[0], i[1])
        compare = i[0]+1 != len(data[1:])
        if compare:
            file.write(f'{indent * i[0]}class {name}:\n{indent * i[0]}\n')
        elif not compare:
            file.write(f'{indent * i[0]}def {name}():\n{indent * i[0]}    """\n{indent * i[0]}    {" ".join(info)}\n{indent * i[0]}    """\n{indent * i[0]}    return "{" ".join(data)}"\n\n')

    # print(TEMP)

# Запрос перечня ссылок на группы комманд
def xapi_cmd(url='https://roomos.cisco.com/xapi?Product=hopen', output_file_name=None):
    '''Get links on command groups'''
    with open(f'pyRoomOSxAPI/{output_file_name}', 'w', encoding='utf-8') as file:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(1)

        # Пакуем группы команд
        reference = driver.find_element(By.CLASS_NAME, 'sub-menu').text.split('\n')

        # Перебор xCommand
        driver.find_element(
            By.CSS_SELECTOR,
            "#app > div > form > div.type-buttons.filter > button:nth-child(2)"
            ).click()

        for i in enumerate(reference):
            driver.find_element(
                By.XPATH,
                f'//a[contains(@href,"/xapi/domain/?domain={reference[i[0]]}")]'
                ).click()

            command_line = ['.'.join(p) for p in [c.split()[1:] for c in [c.text for c in driver.find_elements(By.CLASS_NAME, 'node-path')]]]
            for j in enumerate(command_line):
                driver.find_element(
                    By.XPATH,
                    f'//a[contains(@href,"/xapi/Command.{command_line[j[0]]}/")]'
                    ).click()

                try:
                    driver.find_element(By.CLASS_NAME, 'switcher').click()
                    switcher = driver.find_element(
                        By.CLASS_NAME,
                        'language-javascript'
                        ).text.split()

                    info = driver.find_element(By.CLASS_NAME, 'info').text.split()
                except:
                    pass

                # try:
                #     param = driver.find_element(By.CLASS_NAME, 'param').text
                #     print(f"'''\n{param}\n'''\n\n")
                #     file.write(f"'''\n{param}\n'''\n\n")
                # except:
                #     pass

                # try:
                #     props = driver.find_element(By.CLASS_NAME, 'props').text
                #     print(f"'''\n{props}\n'''\n\n")
                #     file.write(f"'''\n{props}\n'''\n\n")
                # except:
                #     pass

                generator(data=switcher, file=file, info=info)

xapi_cmd(output_file_name='xCommand.py')
