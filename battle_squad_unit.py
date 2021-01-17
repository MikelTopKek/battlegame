import storage
from baseunit import BaseUnit
from data import WarStatuses, TypeOfUnit


class Unit(BaseUnit):
    get_storage_status: str

    def attack(self, *args, **kwargs):
        pass

    @property
    def status(self):
        return getattr(storage.Storage, self.get_storage_status)(self.index)


class BattleUnit(Unit):
    health_points: int
    damage: int
    status = WarStatuses.STATUS_ALIVE

    def __init__(self, index: int):
        super(BattleUnit, self).__init__(index)
        self.squad_index = 0

    def attack(self, enemy):

        enemy.health_points -= self.damage
        enemy.status = WarStatuses.STATUS_DEAD if enemy.health_points <= 0 else WarStatuses.STATUS_ALIVE
        storage.Storage.update_unit(enemy)


class SquadUnit(Unit):
    army_index: int = None
    status = WarStatuses.STATUS_ALIVE

    def __init__(self, index: int):
        super(SquadUnit, self).__init__(index)
        self.index = index

    def attack(self, enemy):
        list_of_squad_self_units = storage.Storage.fill_squad(self.index)
        list_of_squad_enemy_units = storage.Storage.fill_squad(enemy.index)
        if storage.Storage.squad_status(list_of_squad_enemy_units) is WarStatuses.STATUS_DEAD:
            return

        for self_unit in list_of_squad_self_units:
            if self_unit.status is WarStatuses.STATUS_ALIVE:
                enemy_unit = storage.Storage.find_free_unit_in_squad(list_of_squad_enemy_units)
                if enemy_unit:
                    self_unit.attack(enemy_unit)
