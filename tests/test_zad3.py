import pytest
from zad3 import samdlin, naibolvs
@pytest.mark.parametrize("a", ["asd  er qr ewq qr eeeee","tititi e wq w rer rer rer"])
@pytest.mark.parametrize("vivo1", [5,6])
@pytest.mark.parametrize("vivo2", ["qr","rer"])
class testclass:
    def testsamdlin(a,vivo1):
        assert samdlin(a)==vivo1
    def testnaibolvs(a,vivo2):
        assert naibolvs(a)==vivo2