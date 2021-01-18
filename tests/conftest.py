import pytest

from storage import Storage


@pytest.fixture(autouse=True)
def clear_storage():
    """
    Fixture for cleaning Storage before test cases
    """
    Storage.list_of_armies = []
    Storage.list_of_units = []
    Storage.list_of_squads = []
    Storage.countries = []

    Storage._current_unit_index = 0
    Storage._current_squad_index = 0
    Storage._current_army_index = 0

    yield


@pytest.fixture
def human_count():
    some_result = 2
    yield some_result
