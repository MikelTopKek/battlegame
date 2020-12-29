class Country:

    def __init__(self, name, index, human_count, tank_count, human_squads_per_army, tank_squads_per_army,
                 tank_per_squad, human_per_squad):
        self.name = name
        self.index = index
        self.human_count = human_count
        self.tank_count = tank_count
        self.human_squads_per_army = human_squads_per_army
        self.tank_squads_per_army = tank_squads_per_army
        self.tank_per_squad = tank_per_squad
        self.human_per_squad = human_per_squad
        self.list_of_humans = []

    def generate_units(self):
        for i in range(1, self.human_count):
            self.list_of_humans[i] = i

        for i in range(1, self.tank_count):
            self.list_of_humans[i] = i
