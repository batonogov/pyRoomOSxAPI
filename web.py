from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time


# Запрос перечня ссылок на группы комманд
def xapi_cmd(url='https://roomos.cisco.com/xapi?Product=hopen&Type=Command', wait=5):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    return [c for c in driver.find_element(By.CLASS_NAME, 'sub-menu').text.split() if c.isalnum()]

# Генерация ссылки на список существущих комманд в группе
def link_generator(group) -> str:
    return f'https://roomos.cisco.com/xapi/domain/?domain={group}&Product=hopen&Type=Command'

# Получение функционала в зависимости от класса
def get_info(url, name=None, driver_method=None, action=None):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    if driver_method == 'find_elements':
        return [xCommand.text for xCommand in driver.find_elements(By.CLASS_NAME, name)]
    elif driver_method == 'find_element':
        if action:
            commandline_btn = driver.find_element(By.CLASS_NAME, name)
            commandline_btn.click()
            return driver.find_element(By.CLASS_NAME, 'language-javascript').text
        return driver.find_element(By.CLASS_NAME, name).text

# Генерация ссылки на описание комманды
def link_description_generator(command) -> str:
    return f'https://roomos.cisco.com/xapi/Command.{command}?p=havella'
    
groups = xapi_cmd()
# print('groups:', groups)

links = [link_generator(g) for g in groups]
# print('links:', links)

commands = [c.split()[1:] for c in [get_info(url=u, name='node-path', driver_method='find_elements') for u in links[0:1]][0]]
# print('commands:', commands)

valhalla = [link_description_generator('.'.join(p)) for p in commands]
# print('valhalla:', valhalla)

for u in valhalla:
    try:
        print(get_info(url=u, name="switcher", driver_method='find_element', action=True))
    except:
        pass
    
    try:
        print()
        print(get_info(url=u, name="info", driver_method='find_element'))
    except:
        pass

    try:
        print()
        print(get_info(url=u, name="param", driver_method='find_element'))
    except:
        pass
