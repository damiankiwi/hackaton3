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