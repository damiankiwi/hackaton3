def test_chrome(chrome_driver):
    chrome_driver.get('https://testuj.pl/')
    wait = WebDriverWait(chrome_driver, 10)
    cookie = (By.CSS_SELECTOR, "[class='cookie']")
    wait.until(EC.element_to_be_clickable(cookie))
    chrome_driver.find_element(By.CSS_SELECTOR, "[class='agree right']").click()
    chrome_driver.maximize_window()