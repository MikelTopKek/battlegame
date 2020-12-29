from countries import Country
from data import COUNTRY_DATA
from storage import Storage


class War:

    def __init__(self, number_of_countries, number_of_turns):
        self.number_of_turns = number_of_countries
        self.number_of_countries = number_of_turns

    def start_battle(self):
        pass

    def generate(self):
        for i in range(self.number_of_countries):
            country = Country(**COUNTRY_DATA[i])

            Storage.countries.append(country)
