import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
# Use PYTHONPATH=src pytest src/test/test_lcs.py in terminal if VSCode test does not work
from src.main.lcs import *

def test_get_lcs():
    """
    Testing get_lcs function in lcs.py.
    This is to ensure that the get_lcs function is working as intended.
    """
    s1 = "mangoes"
    s2 = "mementos"
    lcs, test1_lcs_length = get_lcs(s1, s2)
    assert test1_lcs_length == 4 # mnos
    
    s3 = "abcdef"
    s4 = "abcdef"
    lcs, test2_lcs_length = get_lcs(s3, s4)
    assert test2_lcs_length == 6 # abcdef
    
    s5 = ""
    s6 = ""
    lcs, test3_lcs_length = get_lcs(s5, s6)
    assert test3_lcs_length == 0 
    
    s7 = "thisisatest"
    s8 = "testing123"
    lcs, test4_lcs_length = get_lcs(s7, s8)
    assert test4_lcs_length == 4 # tsist
    
    s9 = "12345"
    s10 = "54321"
    lcs, test4_lcs_length = get_lcs(s9, s10)
    assert test4_lcs_length == 1 # 5

"""
Testing lcs_string function in lcs.py
TODO: test for proper lcs output
"""
def test_lcs_string():
    """
    Testing lcs_string function in lcs.py.
    This is to ensure that the lcs_string function is working as intended.
    """
    s1 = "mangoes"
    s2 = "mementos"
    lcs1, lcs_length1 = get_lcs(s1, s2)
    
    s3 = "abcdef"
    s4 = "abcdef"
    lcs2, lcs_length2 = get_lcs(s3, s4)
    
    s5 = ""
    s6 = ""
    lcs3, lcs_length3 = get_lcs(s5, s6)
    
    s7 = "thisisatest"
    s8 = "testing123"
    lcs4, lcs_length4 = get_lcs(s7, s8)
    
    s9 = "12345"
    s10 = "54321"
    lcs5, lcs_length5 = get_lcs(s9, s10)
    
    lcs_str1 = lcs_string(s1, s2, lcs1)
    lcs_str2 = lcs_string(s3, s4, lcs2)
    lcs_str3 = lcs_string(s5, s6, lcs3)
    lcs_str4 = lcs_string(s7, s8, lcs4)
    lcs_str5 = lcs_string(s9, s10, lcs5)
    
    assert all([
        lcs_str1 == "mnos",         
        lcs_str2 == "abcdef",       
        lcs_str3 == "",             
        lcs_str4 == "test",
        lcs_str5 == "5"
    ])
    