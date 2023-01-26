from TitanicData import DataExplorer
import pandas as pd

data = pd.read_csv("train.csv")
explorer = DataExplorer(data)

def start_cli(self):

    while True:
        print("Co chcesz zobaczyć? (wpisz 'koniec', aby zakończyć)")
        print("1. Liczbę ofiar w zależności od płci")
        print("2. Histogram wieku ofiar")
        print("3. Szansę na przeżycie w zależności od płci")
        print("4. Szansę na przeżycie w zależności od wieku")
        print("5. Szansę na przeżycie w zależności od klasy biletu\n")

        choice = input('Wprowadź co chcesz wykonać: ')
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
        elif choice == "koniec":
            break

start_cli(explorer)