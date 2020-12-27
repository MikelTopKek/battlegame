class Country:

    def __init__(self, name, index, human_count, tank_count, human_squads_per_army, tank_squads_per_army,
                 tank_per_squad, human_per_squad):
        self.name = name
        self.index = index
        self.humanCount = human_count
        self.tankCount = tank_count
        self.humanSquadsPerArmy = human_squads_per_army
        self.tankSquadsPerArmy = tank_squads_per_army
        self.tankPerSquad = tank_per_squad
        self.humanPerSquad = human_per_squad
        self.list_of_humans = []

    def generate_units(self):
        for i in range(1, self.humanCount):
            self.list_of_humans[i] = i

        for i in range(1, self.tankCount):
            self.list_of_humans[i] = i
