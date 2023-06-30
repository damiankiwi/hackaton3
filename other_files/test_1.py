def test_performance_loading_speed(chrome_driver):
    print()
    start_time = time.time()
    chrome_driver.get("https://testuj.pl/")
    end_time = time.time()
    load_time = end_time - start_time
    print(f'Czas ładowania strony: {load_time} sekund')