from enum import Enum

COUNTRY_DATA = [
    {
        'index': 'test',
        'name': 'TEST',
        'human_count': 6,
        'tank_count': 3,
        'tank_per_squad': 1,
        'human_per_squad': 2,
        'human_squads_per_army': 2,
        'tank_squads_per_army': 1
    },
    {
        'index': 'TheKek',
        'name': 'TheKek',
        'human_count': 6,
        'tank_count': 3,
        'tank_per_squad': 1,
        'human_per_squad': 1,
        'human_squads_per_army': 2,
        'tank_squads_per_army': 1
    },
    {
        'index': 'kfc',
        'name': 'KFC',
        'human_count': 159,
        'tank_count': 21,
        'tank_per_squad': 5,
        'human_per_squad': 33,
        'human_squads_per_army': 2,
        'tank_squads_per_army': 1
    },
    {
        'index': 'ua',
        'name': 'Ukraine',
        'human_count': 112,
        'tank_count': 28,
        'tank_per_squad': 4,
        'human_per_squad': 21,
        'human_squads_per_army': 3,
        'tank_squads_per_army': 1
    }
]


class WarStatuses(Enum):
    STATUS_DEAD = 0
    STATUS_ALIVE = 1
