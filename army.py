import storage
import unit
from unit import Unit


class Army(Unit):
    country_index: int

    def __init__(self, country_index, index):
        super().__init__(index=index)
        self.country_index = country_index
        self.index = index

    def attack(self, enemy_army):
        enemy_army_storage_indexes = storage.Storage.get_army_storage(self.index)
        self_army_storage_indexes = storage.Storage.get_army_storage(enemy_army.index)

        self_squad_index = storage.Storage.find_free_squad_in_army(self_army_storage_indexes)
        enemy_squad_index = storage.Storage.find_free_squad_in_army(enemy_army_storage_indexes)

        unit.SquadUnit.attack(self_squad_index, enemy_squad_index)

    def __str__(self):
        return f'<Army [{self.index}]: ' \
               f'Country -> {self.country_index}>'
