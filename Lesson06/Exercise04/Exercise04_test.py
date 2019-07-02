import import_ipynb
import Exercise04

def test_d1():
    assert str(Exercise04.d1) == "2019-02-25 10:50:00+00:00"


def test_d2():
    assert str(Exercise04.d2) == "2019-02-26 11:20:00+00:00"


def test_d2_madrid():
    assert str(Exercise04.td) == "1 day, 0:30:00"
