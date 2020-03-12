from __future__ import unicode_literals

import os
import re
import codecs
import os
from configparser import ConfigParser
from opynions.parsing import get_file_content
import re

import pytest
import pdb


@pytest.fixture(scope='module')
def get_openedx_yaml():
    """Fixture containing the text content of setup.py"""
    return get_file_content('openedx.yaml')

def test_owner(get_openedx_yaml, results_bag):
    """ Test if owner line exists and get owner name """
    #TODO(jinder): decide how flexible do we want to be with this, the code below is unforgiving
    openedx_file = get_openedx_yaml
    regex_patter = "(?<=owner: )'.*'"
    m = re.search(regex_patter, openedx_file)
    assert m is not None
    owner = m.group(0).replace("'","")
    results_bag.owner = owner

def test_nick(get_openedx_yaml, results_bag):
    """ Test if nick line exists and get nick """
    #TODO(jinder): decide how flexible do we want to be with this, the code below is unforgiving
    openedx_file = get_openedx_yaml
    regex_patter = "(?<=nick: ).*\n"
    m = re.search(regex_patter, openedx_file)
    assert m is not None
    nick = m.group(0).replace("\n","")
    results_bag.owner = nick
