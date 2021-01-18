class EmptySquadList(Exception):
    pass


class ArmyIsDeadException(Exception):
    def __init__(self, army_id, *args, **kwargs):
        self.army_id = army_id
        super().__init__(*args, **kwargs)
