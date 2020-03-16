from __future__ import unicode_literals

import os
import re
import codecs
import os
from configparser import ConfigParser
from opynions.parsing import get_file_content
import re
import pdb

import pytest


@pytest.fixture(scope='module')
def get_openedx_yaml():
    """Fixture containing the text content of setup.py"""
    return get_file_content('openedx.yaml')

def test_owner(get_openedx_yaml, results_bag):
    """ Test if owner line exists and get owner name """
    #TODO(jinder): decide how flexible do we want to be with this, the code below is unforgiving
    openedx_file = get_openedx_yaml
    regex_pattern = "(?<=owner: ).*"
    m = re.search(regex_pattern, openedx_file)
    results_bag.has_owner = False
    assert m is not None
    results_bag.has_owner = True

    owner = m.group(0).replace("'","")
    results_bag.owner = owner

def test_nick(get_openedx_yaml, results_bag):
    """ Test if nick line exists and get nick """
    #TODO(jinder): decide how flexible do we want to be with this, the code below is unforgiving
    openedx_file = get_openedx_yaml
    regex_pattern = "(?<=nick: ).*\n"
    m = re.search(regex_pattern, openedx_file)
    results_bag.has_nick = False
    assert m is not None
    results_bag.has_nick = True
    nick = m.group(0).replace("\n","")
    results_bag.nick = nick
