import pytest
from zad2 import zad2,dlinastr,strokBezposl
@pytest.mark.parametrize("a", ["ccdfrferh","ertert213hth 4","rt"])
@pytest.mark.parametrize("vivo1", ["найден символ с",None,None])
@pytest.mark.parametrize("vivo2", [9,14,2])
@pytest.mark.parametrize("vivo3", ['ccdfrfer','ertert213hth ','r'])
class test_class:
    def test_zad2(a,vivo1):
        assert zad2(a)==vivo1
    def test_dlina(a,vivo2):
        assert dlinastr(a)==vivo2
    def test_strokB(a,vivo3):
        assert strokBezposl(a)==vivo3