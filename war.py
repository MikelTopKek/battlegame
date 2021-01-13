from data import COUNTRY_DATA
from storage import Storage


class War:

    def start_battle(self):
        pass

    def generate(self):
        for country in COUNTRY_DATA:
            Storage.add_country(**country)
