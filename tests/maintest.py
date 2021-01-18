from unittest.mock import patch

from storage import Storage
from war import War


def test_human_creation(human_count):
    Storage.add_humans(human_count)
    assert len(Storage.list_of_units) == human_count

    expected_human_indexes = [0, 1]
    assert [h.index for h in Storage.list_of_units] == expected_human_indexes

    for human in Storage.list_of_units:
        assert human.health_points > 0
        assert human.damage > 0

# @patch('units.some_data', 567)
# @patch('units.random.randint')  # -> 2
# @patch('units.random.randint')  # -> 1
# def test_human_health_creation(mocked_randint, mocked_randint_2):
#     mocked_randint.side_effect = lambda: 4
#     Storage.add_humans(1)


@patch('units.random.randint')
def test_human_health_creation(mocked_randint):
    mocked_health_points = 4
    mocked_randint.side_effect = lambda *args, **kwargs: mocked_health_points

    Storage.add_humans(1)

    assert mocked_randint.call_count == 2
    assert Storage.list_of_units[0].health_points == mocked_health_points


# def test_war_creation_structure():
#     w = War()
#     w.generate()
#
#     assert ...
