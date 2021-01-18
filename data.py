from enum import Enum

COUNTRY_DATA = [
    {
        'index': 'gondurass',
        'name': 'GONDURASS',
        'human_count': 19,
        'tank_count': 8,
        'tank_per_squad': 2,
        'human_per_squad': 3,
        'human_squads_per_army': 3,
        'tank_squads_per_army': 2
    },
    {
        'index': 'TheKek',
        'name': 'TheKek',
        'human_count': 65,
        'tank_count': 7,
        'tank_per_squad': 2,
        'human_per_squad': 4,
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
