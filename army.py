import storage
from battle_squad_unit import Unit
from data import WarStatuses


class Army(Unit):
    country_index: int

    def __init__(self, country_index, index):
        super().__init__(index=index)
        self.country_index = country_index
        self.index = index

    def attack(self, enemy_army):
        list_of_squads_enemy_army = storage.Storage.get_army_storage(self.index)
        list_of_squads_self_army = storage.Storage.get_army_storage(enemy_army.index)

        for self_squad in list_of_squads_self_army:
            if self_squad.status is WarStatuses.STATUS_DEAD:
                break
            enemy_squad = storage.Storage.find_free_squad_in_army(list_of_squads_enemy_army)
            if enemy_squad:
                self_squad.attack(enemy_squad)

    def __str__(self):
        return f'<Army [{self.index}]: ' \
               f'Country -> {self.country_index}>'
