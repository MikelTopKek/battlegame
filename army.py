from unit import Unit


class Army(Unit):
    country_index: int

    def __init__(self, country_index, index):
        super().__init__(index=index)
        self.country_index = country_index

    def attack(self, *args, **kwargs):
        pass

    def __str__(self):
        return f'<Army [{self.index}]: ' \
               f'Country -> {self.country_index}, ...>'