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