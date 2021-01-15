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

        if self.status == WarStatuses.STATUS_DEAD or enemy.status == WarStatuses.STATUS_DEAD:
            return

        enemy.health_points -= self.damage
        self.health_points -= enemy.damage

        new_status_self = WarStatuses.STATUS_DEAD if self.health_points <= 0 else WarStatuses.STATUS_ALIVE
        new_status_enemy = WarStatuses.STATUS_DEAD if enemy.health_points <= 0 else WarStatuses.STATUS_ALIVE

        unit_type_enemy = storage.Storage.get_essence_type(self)
        unit_type_self = storage.Storage.get_essence_type(enemy)
        if unit_type_enemy == TypeOfUnit.TYPE_HUMAN:
            storage.Storage.update_human(enemy.index, enemy.health_points, new_status_enemy)
        else:
            storage.Storage.update_tank(enemy.index, enemy.health_points, new_status_enemy)

        if unit_type_self == TypeOfUnit.TYPE_HUMAN:
            storage.Storage.update_human(self.index, self.health_points, new_status_self)
        else:
            storage.Storage.update_tank(self.index, self.health_points, new_status_self)


class SquadUnit(Unit):
    army_index: int = None
    status = WarStatuses.STATUS_ALIVE

    def __init__(self, index: int):
        super(SquadUnit, self).__init__(index)
        self.index = index

    def attack(self, enemy_squad_index):

        self_squad_type = storage.Storage.get_essence_type(self)
        enemy_squad_type = storage.Storage.get_essence_type(enemy_squad_index)
        if storage.Storage.squad_status(enemy_squad_index, enemy_squad_type) == WarStatuses.STATUS_ALIVE:

            self_unit = storage.Storage.find_free_unit_in_squad(self, self_squad_type)
            enemy_unit = storage.Storage.find_free_unit_in_squad(enemy_squad_index, enemy_squad_type)

            self_unit.attack(enemy_unit)
