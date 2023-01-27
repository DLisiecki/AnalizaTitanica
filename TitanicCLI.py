from TitanicData import DataExplorer
import pandas as pd

# Wczytanie pliku train.csv jako obiekt DataFrame
data = pd.read_csv("train.csv")

# Obiekt klasy DataExplorer z wczytanego wczesniej pliku
explorer = DataExplorer(data)

def start_cli(self):
    # Pętla, która pozwala na wybór opcji z menu
    while True:
        print("Co chcesz zobaczyć? (wpisz 'koniec', aby zakończyć)")
        print("1. Liczbę ofiar w zależności od płci")
        print("2. Histogram wieku ofiar")
        print("3. Szansę na przeżycie w zależności od płci")
        print("4. Szansę na przeżycie w zależności od wieku")
        print("5. Szansę na przeżycie w zależności od klasy biletu")
        print("6. Liczbę ofiar vs ocalałych \n")

        choice = input('Wprowadź co chcesz wykonać: ')
        # Sprawdzanie wyboru użytkownika i wywołanie odpowiedniej metody
        if choice == "1":
            self.show_victims_by_sex()
        elif choice == "2":
            self.show_age()
        elif choice == "3":
            self.show_survival_rate_by_sex()
        elif choice == "4":
            self.show_survival_rate_by_age()
        elif choice == "5":
            self.show_survival_rate_by_class()
        elif choice == "6":
            self.show_survival_rate()
        elif choice == "koniec":
            break

# uruchamianie funkcji
start_cli(explorer)