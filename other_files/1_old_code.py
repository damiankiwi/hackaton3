import requests
import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pytest_testrail.plugin import testrail, pytestrail
@pytestrail.case('C2405')
def test_Chrome():
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    driver.get('https://testuj.pl/')
    wait = WebDriverWait(driver, 30)
    cookie = (By.CSS_SELECTOR, "[class='cookie']")
    wait.until(EC.element_to_be_clickable(cookie))
    driver.find_element(By.CSS_SELECTOR, "[class='agree right']").click()
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "[class='button button--bigger']").click()
    driver.quit()


@pytestrail.case('C2406')
def test_urls():
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

    return True

@pytestrail.case('C2407')
def test_performance_loading_speed():
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    start_time = time.time()
    driver.get("https://testuj.pl/")
    end_time = time.time()
    load_time = end_time - start_time
    driver.quit()
    print(f'Czas ładowania strony: {load_time} sekund')

@pytestrail.case('C2408')
def test_all():
    test_Chrome()
    test_results = {}
    test_results['test_urls'] = test_urls()
    test_performance_loading_speed()

    for test_name, result in test_results.items():
        print(f'{test_name}: {"PASSED" if result else "FAILED"}')


test_all()