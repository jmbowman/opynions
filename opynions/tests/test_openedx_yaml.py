from __future__ import unicode_literals

import os
import re
import codecs
import os
from configparser import ConfigParser
from opynions.parsing import get_file_content

import pytest


@pytest.fixture(scope='module')
def get_openedx_yaml():
    """Fixture containing the text content of setup.py"""
    return get_file_content('openedx.yaml')

def test_something(get_openedx_yaml, results_bag):
    openedx_file = get_openedx_yaml
    results_bag.test_value = "hahahha"
    assert 1 == 1