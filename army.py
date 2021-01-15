import storage
from unit import Unit


class Army(Unit):
    country_index: int

    def __init__(self, country_index, index):
        super().__init__(index=index)
        self.country_index = country_index

    def attack(self, enemy_army):
        enemy_army_country = storage.Storage.return_army_country(enemy_army)

        self_squad = storage.Storage.find_free_squad_in_army(self.index)
        enemy_squad = storage.Storage.find_free_squad_in_army(enemy_army)

        self_squad.attack()

        print(self_squad)
        print(enemy_squad)



    def __str__(self):
        return f'<Army [{self.index}]: ' \
               f'Country -> {self.country_index}>'
