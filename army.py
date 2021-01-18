import storage
from battle_squad_unit import Unit
from data import WarStatuses


class Army(Unit):
    country_index: int
    status = WarStatuses.STATUS_ALIVE

    def __init__(self, country_index, index):
        super().__init__(index=index)
        self.country_index = country_index
        self.index = index

    def attack(self, enemy_army):
        list_of_squads_enemy_army = storage.Storage.get_army_storage(enemy_army.index)
        list_of_squads_self_army = storage.Storage.get_army_storage(self.index)
        if len(list_of_squads_enemy_army) == 0 or len(list_of_squads_self_army) == 0:
            return
        for self_squad in list_of_squads_self_army:
            if self_squad.status is WarStatuses.STATUS_DEAD or len(list_of_squads_enemy_army) == 0:
                break
            enemy_squad = storage.Storage.find_free_squad_in_army(list_of_squads_enemy_army, self.index)
            if not enemy_squad:
                return
            if enemy_squad.status is not WarStatuses.STATUS_DEAD:
                self_squad.attack(enemy_squad)
        storage.Storage.update_army_status(enemy_army)

    def __str__(self):
        return f'<Army [{self.index}]: ' \
               f'Country -> {self.country_index}>'
