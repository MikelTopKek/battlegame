from data import COUNTRY_DATA
from data import WarStatuses
from storage import Storage
from random import seed, shuffle, randint


class War:
    number_of_countries = 0

    def generate(self):
        for country in COUNTRY_DATA:
            Storage.add_country(**country)
            self.number_of_countries += 1

    def start_battle(self):

        battle_list = self.generate_opponents_distribution()
        print(battle_list)
        j = 0
        while j < 50:
            for i in range(0, self.number_of_countries):
                list_of_armies_enemy_country = Storage.get_country_storage(Storage.countries[battle_list[i]].index)
                list_of_armies_self_country = Storage.get_country_storage(Storage.countries[battle_list[i+1]].index)
                for self_country in list_of_armies_self_country:
                    if self_country.status is WarStatuses.STATUS_DEAD:
                        break
                    enemy_country = Storage.find_free_army_in_country(list_of_armies_enemy_country)
                    if enemy_country:
                        self_country.attack(enemy_country)
            j += 1

    def generate_opponents_distribution(self):
        seed()
        battle_list = [i for i in range(self.number_of_countries)]
        shuffle(battle_list)
        battle_list.append(randint(0, self.number_of_countries-1))
        while battle_list[-1] == battle_list[-2]:
            battle_list.pop()
            battle_list.append(randint(0, self.number_of_countries-1))
        return battle_list
