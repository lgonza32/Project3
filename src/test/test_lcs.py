import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.main.lcs import *

"""
Testing get_lcs function in lcs.py
TODO: test for proper lcs length
"""
def test_get_lcs():
    s1 = "mangoes"
    s2 = "mementos"
    lcs, test1_lcs_length = get_lcs(s1, s2)
    assert test1_lcs_length == 4

"""
Testing lcs_string function in lcs.py
TODO: test for proper lcs output
"""
def test_lcs_string():
    return 0