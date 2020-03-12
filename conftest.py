import pytest
from pytest_harvest import get_session_results_dct, get_fixture_store
import pprint

pp = pprint.PrettyPrinter(indent=4)


def pytest_sessionfinish(session):
    fixture_store = get_fixture_store(session)
    results_bag = fixture_store['results_bag']
    # results_bag contains any new info stored by tests, 
    # here I would parse through info in results bag and store it in either dict or dataframe
    # and save to file

