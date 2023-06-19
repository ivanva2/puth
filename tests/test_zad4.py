import pytest
from zad4 import kak
@pytest.mark.parametrize("a,rezylt",[("1+2","3"),("2*4","8"),("math.factorial(5)","120"),("math.fabs(-4)","4.0"),("3**3","27")])
def testskalkul(a,rezylt):
    assert kak(a)==rezylt
def test_zero():
    with pytest.raises(ZeroDivisionError):
        kak("10/0")    
def test_NameError():
    with pytest.raises(SyntaxError):
        kak("10tet2")