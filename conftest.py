import pytest
from pytest_harvest import get_session_results_dct, get_fixture_store
import pprint
import pdb

pp = pprint.PrettyPrinter(indent=4)


def pytest_sessionfinish(session):
    fixture_store = get_fixture_store(session)
    results_bag = fixture_store['results_bag']
    for test_name, results in results_bag.items():
        print("    - '%s':" % test_name)
        for output_name, output_value in results.items():
            print("      - '%s': %s" % (output_name, output_value))
    # results_bag contains any new info stored by tests, 
    # here I would parse through info in results bag and store it in either dict or dataframe
    # and save to file

