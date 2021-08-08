from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys


with open('config.py', "r") as file:
    content = file.read()
    config = json.loads(content)



def visit_with_cookies(link_submitted):
    print('visit_with_cookies called', flush=True)

    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options = options, executable_path="/opt/CTF/geckodriver", service_log_path="/opt/CTF/geckodriver.log")
    try:
        browser.set_page_load_timeout(15)
        browser.get(config['host'])
        cookie = {'name' : 'admin',
            'value':'ASV\{C0ok13_th31f\}'}

        browser.add_cookie(cookie)

        browser.get(link_submitted)
        browser.quit()
    except Exception as e:
        print(e, flush=True)
        browser.quit()
        print('Came in the exception loop.', flush=True)

    print('visit_with_cookies function successfully executed', flush=True)


