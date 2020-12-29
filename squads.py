from unit import Unit


class HumanSquad(Unit):

    def __str__(self):
        return f'<HumanSquad[{self.index}>'


class TankSquad(Unit):

    def __str__(self):
        return f'<TankSquad[{self.index}>'
