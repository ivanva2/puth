import pytest
from zad1 import zadanie1

@pytest.mark.parametrize("a,b,vivod",[(1,2,'1-ое число меньше пограничного'),(4,2,'1-ое число больше пограничного'),(9,2,'1-ое число больше пограничного более, чем в 3 раза')])
def test_unt1_positive(a,b,vivod):
    assert zadanie1(a,b)==vivod