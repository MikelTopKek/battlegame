import pytest

from storage import Storage


@pytest.fixture(autouse=True)
def clear_storage():
    """
    Fixture for cleaning Storage before test cases
    """
    Storage.humans = []
    Storage.tanks = []
    Storage.human_squads = []
    Storage.human_squads = []
    Storage.tank_squads = []
    Storage.countries = []
    Storage.armies = []

    Storage._current_human_index = 0
    Storage._current_human_squad_index = 0
    Storage._current_army_index = 0
    Storage._current_tank_index = 0
    Storage._current_tank_squad_index = 0

    yield


@pytest.fixture
def human_count():
    some_result = 2
    yield some_result
