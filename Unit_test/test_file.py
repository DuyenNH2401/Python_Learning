from test import is_valid
import pytest

def test_plates():

    #check length and with alphabet
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFGHIJ") == False
    assert is_valid("A") == False

    #check with 2 letters
    assert is_valid("AA") == True
    assert is_valid("A2") == True
    assert is_valid("2A") == False
    assert is_valid("22") == False

    #number in the middle and zero start of number
    assert is_valid("AB234C") == False
    assert is_valid("AB01") == False
    assert is_valid("AB10") == True

    #space or punctuation
    assert is_valid("AB?123") == False
    assert is_valid("AB_123") == False

test_plates()
