import logging

logging.basicConfig(level=logging.INFO)

def kalkulator():
    print("Podaj działanie, posługując się odpowiednią liczbą: ")
    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")

    dzialanie = input("Wybierz działanie (1, 2, 3, 4): ")

    skladnik1 = float(input("Podaj składnik 1: "))
    skladnik2 = float(input("Podaj składnik 2: "))

    if dzialanie == '1':
        logging.info(f'Dodaję {skladnik1} i {skladnik2}')
        wynik = skladnik1 + skladnik2
    elif dzialanie == '2':
        logging.info(f'Odejmuję {skladnik2} od {skladnik1}')
        wynik = skladnik1 - skladnik2
    elif dzialanie == '3':
        logging.info(f'Mnożę {skladnik1} i {skladnik2}')
        wynik = skladnik1 * skladnik2
    elif dzialanie == '4':
        logging.info(f'Dzielę {skladnik1} przez {skladnik2}')
        wynik = skladnik1 / skladnik2
    else:
        print("Nieprawidłowy wybór działania!")
        return

    print(f"Wynik to: {wynik:.2f}")

if __name__ == "__main__":
    kalkulator()