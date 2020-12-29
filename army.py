from unit import Unit


class Army(Unit):

    def __init__(self, index, country_index):
        super().__init__(index, country_index)
        self.countryIndex = index
