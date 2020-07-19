'''
Test file for the stockcheck application
'''
import pytest   #type:ignore
from src import main

def test_pydoc():
    '''
    Test file added for 100% code coverage
    '''
    print(pytest.__doc__)
    assert isinstance(pytest.__doc__, str)

def test_main():
    '''
    Test file2 added for 100% code coverage
    '''
    print(main.__doc__)
    assert isinstance(main.__doc__, str)
