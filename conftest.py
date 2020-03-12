import pytest
from pytest_harvest import get_session_results_dct, get_fixture_store
import pprint
import pdb

pp = pprint.PrettyPrinter(indent=4)


def pytest_sessionfinish(session):
    fixture_store = get_fixture_store(session)
    results_bag = fixture_store['results_bag']
    pdb.set_trace()
    pp.pprint(results_bag)
