from data import country_data
from storage import Storage
from countries import Country


class War:

    def __init__(self, number_of_countries, number_of_turns):
        self.number_of_turns = number_of_countries
        self.number_of_countries = number_of_turns

    def start_battle(self):
        pass

    def generate(self):
        for i in range(self.number_of_countries):
            country = Country(**country_data[i])

            Storage.countries.append(country)
