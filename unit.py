import storage
from baseunit import BaseUnit
from data import WarStatuses


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

    def __init__(self, index: int, squad_index: int = None):
        super(BattleUnit, self).__init__(index)
        # self.status = WarStatuses.STATUS_ALIVE
        self.squad_index = squad_index

    def attack(self, enemy):
        health_points = enemy.health_points - self.damage

        new_status_enemy = WarStatuses.STATUS_DEAD if health_points <= 0 else None

        storage.Storage.update_human(enemy.index, health_points, new_status_enemy)


class SquadUnit(Unit):
    army_index: int = None
    squad_status = None

    def attack(self, enemy_squad_index):
        pass
