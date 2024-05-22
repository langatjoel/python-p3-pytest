# lib/testing/test_not_none.py

from lib.not_none_functions import return_not_none

def test_return_not_none():
    assert return_not_none() is not None
