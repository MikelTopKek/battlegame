from countries import Country


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Storage(Country):

    def __init__(self):
        self.countries = list()
        self.tankSquads = list()
        self.humanSquads = list()
        self.tanks = list()
        self.humans = list()
        self.armies = list()


