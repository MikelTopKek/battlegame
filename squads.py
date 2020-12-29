from baseunit import SquadUnit


class HumanSquad(SquadUnit):

    def __str__(self):
        return f'<HumanSquad[{self.index}>'


class TankSquad(SquadUnit):

    def __str__(self):
        return f'<TankSquad[{self.index}>'
