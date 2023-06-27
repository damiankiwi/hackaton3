import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
import os
from pytest_testrail.plugin import pytestrail
from datetime import datetime

# # Konfiguracja
# testrail_url = 'https://kiwipythontest.testrail.io/'
# testrail_user = 'kiwipythontest@gmail.com'
# testrail_password = 'Nowehaslo123!'
# testrail_project_id = 3
# testrail_suite_id = 21

@pytest.fixture(scope='session')
def chrome_options():
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return options

@pytest.fixture(scope='session')
def chrome_driver(chrome_options):
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)
    yield driver
    driver.quit()

@pytest.mark.html
@pytestrail.case('C2407')
def test_performance_loading_speed(chrome_driver):
    print()
    start_time = time.time()
    chrome_driver.get("https://testuj.pl/")
    end_time = time.time()
    load_time = end_time - start_time
    print(f'Czas ładowania strony: {load_time} sekund')

@pytest.mark.html
@pytestrail.case('C2405')
def test_chrome(chrome_driver):
    chrome_driver.get('https://testuj.pl/')
    wait = WebDriverWait(chrome_driver, 10)
    cookie = (By.CSS_SELECTOR, "[class='cookie']")
    wait.until(EC.element_to_be_clickable(cookie))
    chrome_driver.find_element(By.CSS_SELECTOR, "[class='agree right']").click()
    chrome_driver.maximize_window()

@pytest.mark.html
@pytestrail.case('C2406')
def test_urls():
    print()
    print('Statusy HTTP:')
    urls = [
        ('O nas', 'https://testuj.pl/o-nas'),
        ('Finansowanie szkoleń', 'https://testuj.pl/finansowanie-szkolen'),
        ('Szkolenia', 'https://testuj.pl/szkolenia'),
        ('Dla firm', 'https://testuj.pl/dla-firm'),
        ('Blog', 'https://testuj.pl/blog'),
        ('Kontakt', 'https://testuj.pl/kontakt')
    ]

    for name, url in urls:
        response = requests.head(url)
        status_code = response.status_code
        print(f'{name}: Status HTTP {status_code}')

if __name__ == "__main__":
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"report_{now}.html"
    pytest.main(['-v', '--html=' + report_path, '--testrail', f'--testrail-url={testrail_url}',
                 f'--testrail-user={testrail_user}', f'--testrail-password={testrail_password}',
                 f'--testrail-project-id={testrail_project_id}', f'--testrail-suite-id={testrail_suite_id}'])


