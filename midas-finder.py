import requests
from bs4 import BeautifulSoup

def szukaj_najtanszych_rzeczy(nazwa_produktu, liczba_wynikow, url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Nie udało się pobrać wyników wyszukiwania.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    wyniki = soup.find_all('div', class_='offer-wrapper')

    for i, wynik in enumerate(wyniki[:liczba_wynikow], start=1):
        nazwa = wynik.find('strong').text.strip()
        cena = wynik.find('p', class_='price').strong.text.strip()
        link = wynik.find('a', class_='marginright5')['href']

        print(f'{i}. {nazwa} - {cena}')
        print(f'   Link: {link}')
        print()

if __name__ == "__main__":
    nazwa_produktu = input("Podaj nazwę produktu, którego najtańsze oferty chcesz znaleźć: ")
    liczba_wynikow = int(input("Podaj liczbę wyników do wyświetlenia: "))

    # Dla OLX.pl
    url_olx = f'https://www.olx.pl/oferty/q-{nazwa_produktu}/?search%5Bfilter_float_price%3Ato%5D=1000&sorting=price_asc&photos=1'

    print("\nWyniki z OLX.pl:")
    szukaj_najtanszych_rzeczy(nazwa_produktu, liczba_wynikow, url_olx)

    # Możesz dodać inne strony, zmieniając URL i analizując strukturę HTML
    # Przykład dla Allegro.pl (sekcja używane):
    # url_allegro = f'https://allegro.pl/listing?string={nazwa_produktu}&order=m&bmatch=baseline-nbn-dict42-ele-1-5-1018'
    # print("\nWyniki z Allegro.pl:")
    # szukaj_najtanszych_rzeczy(nazwa_produktu, liczba_wynikow, url_allegro)