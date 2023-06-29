import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


def test_performance_loading_speed():
    print()
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


def test_chrome():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get('https://testuj.pl/')
    wait = WebDriverWait(driver, 10)
    cookie = (By.CSS_SELECTOR, "[class='cookie']")
    wait.until(expected_conditions.element_to_be_clickable(cookie))
    driver.find_element(By.CSS_SELECTOR, "[class='agree right']").click()
    driver.maximize_window()
    driver.quit()

def test_chrome_python():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get('https://testuj.pl/')
    assert 'testuj.pl' in driver.title
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    cookie = (By.CSS_SELECTOR, "[class='cookie']")
    wait.until(expected_conditions.element_to_be_clickable(cookie))
    driver.find_element(By.CSS_SELECTOR, "[class='agree right']").click()
    driver.find_element(By.CSS_SELECTOR, "[class='button']").click()
    assert driver.find_element(By.CLASS_NAME, 'coursesListHeader__list-url').is_displayed()
    driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys('Python')
    driver.find_element(By.CSS_SELECTOR, "[class='formField__button']").click()
    driver.quit()


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

    return True


if __name__ == "__main__":
    pytest.main()