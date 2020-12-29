from units import Human


class Storage:
    armies: list = list()
    humans = list()
    tanks = list()
    human_squads = list()
    tank_squads = list()
    countries = list()

    @classmethod
    def get_elem_by_index(cls, index: int, elem_type: str) -> list:
        list_data = ...  # TODO:::this data should depends on the elem_type

        # return list(filter(lambda x: x.index == index, list_data))
        # the same here \/
        def filter_rule(x):
            return x.index == index

        return list(filter(filter_rule, list_data))

    @classmethod
    def get_humans_by_squad(cls, squad_index: int) -> list:
        return list(
            filter(
                lambda x: x.squad_index == squad_index,
                cls.humans
            )
        )
