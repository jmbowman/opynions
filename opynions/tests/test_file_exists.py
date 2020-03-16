from __future__ import unicode_literals

import os
import re
import codecs
import os
from configparser import ConfigParser
from opynions.parsing import get_file_names
import re
import glob
import pdb

import pytest

def test_openedx_yaml_exists(results_bag):
    files = [f for f in glob.glob("**/*.yaml", recursive=True)]
    openedx_exists = False
    for file_name in files:
        if "openedx" in file_name:
            openedx_exists = True
    results_bag.has_openedx_yaml = openedx_exists
    assert openedx_exists == True

def test_has_makefile(results_bag):
    files = [f for f in glob.glob("**/Makefile", recursive=True)]
    makefile_exists = False
    for file_name in files:
        if "Makefile" in file_name:
            makefile_exists = True
    results_bag.has_Makefile = makefile_exists
    assert makefile_exists == True
