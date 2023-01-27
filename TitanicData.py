import pandas as pd
import matplotlib.pyplot as plt


class DataExplorer:

    def __init__(self, data):
        self.data = data

    def show_victims_by_sex(self):
        # Wyświetla liczbę ofiar podzieloną na płeć

        data_by_sex = self.data.groupby("Sex")
        data_by_sex_count = data_by_sex.count()

        plt.bar(data_by_sex_count.index, data_by_sex_count["Survived"], color=['#1f77b4', '#ff7f0e'])
        plt.xlabel("Płeć")
        plt.ylabel("Liczba ofiar")
        plt.xticks(data_by_sex_count.index, ["Kobiety", "Mężczyźni"])
        plt.grid(axis='y')
        plt.show()

    def show_age(self):
        #Wyświetla histogram wieku ofiar dla mężczyzn i kobiet

        male_data = self.data[self.data["Sex"] == "male"]
        female_data = self.data[self.data["Sex"] == "female"]

        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        axs[0].hist(male_data["Age"], bins=20, color="#1f77b4", width = 2.6, alpha=0.8)
        axs[0].set_xlabel("Wiek")
        axs[0].set_ylabel("Liczba ofiar")
        axs[0].set_title("Mężczyzni")
        plt.grid(axis='y')

        axs[1].hist(female_data["Age"], bins=20, color="#ff7f0e", width = 2.3, alpha=0.8)
        axs[1].set_xlabel("Wiek")
        axs[1].set_ylabel("Liczba ofiar")
        axs[1].set_title("Kobiety")

        plt.grid(axis='y')
        plt.show()

    def show_survival_rate_by_sex(self):
        # Wyświetla szansę przeżycia dla mężczyzn i kobiet w formie wykresu kołowego

        data_by_sex = self.data.groupby("Sex")
        data_by_sex_survived = data_by_sex["Survived"].mean()

        labels = ['Mężczyźni', 'Kobiety']
        sizes = [data_by_sex_survived['male'], data_by_sex_survived['female']]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.title("Przetrwanie w podziale na mężczyzn i kobiet")
        plt.show()

    def show_survival_rate_by_age(self):
        #Wyświetla szanse na przeżycie z uwzględnieniem klasy biletu

        bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        self.data['AgeBin'] = pd.cut(self.data['Age'], bins)

        data_by_age_bin = self.data.groupby(['AgeBin'])
        data_by_age_bin_survived = data_by_age_bin["Survived"].mean()
        data_by_age_bin_survived = data_by_age_bin_survived * 100
        data_by_age_bin_survived.plot(kind='bar', color='#ff7f0e', width = 0.9)

        plt.xlabel("Przedział wiekowy")
        plt.ylabel("Szansa na przeżycie [%]")
        plt.title("Szansa na przeżycie w zależności od przedziału wiekowego")
        plt.show()

    def show_survival_rate_by_class(self):
        # Wyświetla liczbe ofiar i przeżytych uwzględniając klase biletu

        data_by_class = self.data.groupby("Pclass")
        class_survived = data_by_class.sum()['Survived']
        class_not_survived = data_by_class.count()['Survived'] - class_survived

        class_not_survived.name = 'Zgineli'
        class_survived.name = 'Przeżyli'
        survival_data = pd.concat([class_not_survived, class_survived], axis=1)
        survival_data.plot(kind='bar', stacked=True)

        plt.xlabel("Klasa biletu")
        plt.ylabel("Liczba ofiar")
        plt.title("Szansa na przeżycie w zależności od klasy biletu")
        plt.grid(axis='y')
        plt.show()

    def show_survival_rate(self):
        # Wyświetla w % liczbę ocalałych vs ofiar w wykresie kołowym

        data_by_survival = self.data.groupby("Survived")
        data_by_survival_count = data_by_survival["PassengerId"].count()

        labels = ['Ofiary', 'Ocaleni']
        sizes = [data_by_survival_count[0], data_by_survival_count[1]]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.title("Podział na ofiary i ocalonych")
        plt.show()



